/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package controller;

import java.io.IOException;
import java.sql.SQLException;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.LinkedList;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import model.ReservationModel;
import model.RestaurantModel;
import utils.Validator;

/**
 *
 * @author benha
 */
@WebServlet(name = "RestaurantController", urlPatterns = {"/RestaurantController"})
public class RestaurantController extends HttpServlet {
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doPost(request,response);
    }
    
    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String action = request.getParameter("action");
        if("sign_up".equals(action)){
            String email = request.getParameter("Restaurant_Email");
            String password = request.getParameter("Restaurant_Password");
            String restaurantName = request.getParameter("Name");
            String addressLine1 = request.getParameter("Address_Line1");
            String area = request.getParameter("Area").toLowerCase();
            String postCode = request.getParameter("PostCode");
            String contactNumber = request.getParameter("Contact_Number");
            String foodType = request.getParameter("Food_Type");
            String stringTotalNumberOfSeats = request.getParameter("Total_No_Seats");
            
            if(email != null && password != null && restaurantName != null &&  addressLine1 != null && area != null
                    && postCode != null && contactNumber != null && foodType != null && stringTotalNumberOfSeats != null){
                try{
                    int totalNumberOfSeats = Integer.parseInt(stringTotalNumberOfSeats);
                    boolean signupResult = this.signup(email, password, restaurantName, addressLine1, area,
                                                      postCode, contactNumber, foodType, totalNumberOfSeats);
                    
                    if(signupResult){
                        RequestDispatcher view = request.getRequestDispatcher("index.jsp");
                        view.forward(request, response);
                    }
                    else{
                        response.sendRedirect("errorPage.html");
                    }
                }
                catch(Exception e){
                    response.sendRedirect("errorPage.html");
                }
            }
        }
        else if("view_reservations".equals(action)){
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            String typeOfUser = (String) sess.getAttribute("type_of_user");
            if (email != null && typeOfUser != null) {
                try {
                    ReservationModel resModel = ReservationModel.getInstance();
                    LinkedList<ReservationModel> reservationList = resModel.selectAllReservationByRestaurantEmail(email);
                    request.setAttribute("reservationList", reservationList);
                    RequestDispatcher view = request.getRequestDispatcher("RestaurantViewReservations.jsp");
                    view.forward(request, response);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        else if("update".equals(action)){
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            
            String contactNumber = request.getParameter("Contact_Number");
            String monToFryOt = request.getParameter("MondayToFriday_OT");
            String monToFryCt = request.getParameter("MondayToFriday_CT");
            String satOt = request.getParameter("Sat_OT");
            String satCt = request.getParameter("Sat_CT");
            String sunOt = request.getParameter("Sun_OT");
            String sunCt = request.getParameter("Sun_CT");
            int totalNumberOfSeats = Integer.parseInt(request.getParameter("Total_No_Seats"));
            if (email != null) {
                try {
                    boolean result = this.update(monToFryOt,monToFryCt,satOt,satCt,sunOt,sunCt,totalNumberOfSeats,contactNumber,email);
                    if(!result){
                        response.sendRedirect("errorPage.html");
                    }
                    else{
                        RequestDispatcher view = request.getRequestDispatcher("RestaurantMenu.html");
                        view.forward(request, response);
                    }
                } catch (Exception e) {
                    response.sendRedirect("errorPage.html");
                }
            }
        }
        else if("update_number_of_seats".equals(action)){
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            int bookedSeats = Integer.parseInt(request.getParameter("Booked_seats"));
            if (email != null) {
                try {
                    if(!this.updateNumberOfSeats(bookedSeats,email)){
                        response.sendRedirect("errorPage.html");
                    }
                    else{
                        RequestDispatcher view = request.getRequestDispatcher("RestaurantMenu.html");
                        view.forward(request, response);
                    }
                } catch (Exception e) {
                    response.sendRedirect("errorPage.html");
                }
            }
        }
    }
    
    /**
     * updates restaurant data
     * @param monToFryOt the opening time that goes from monday to friday
     * @param monToFryCt the closing time that goes from monday to friday
     * @param satOt saturday opening time
     * @param satCt saturday closing time
     * @param sunOt sunday opening time
     * @param sunCt sunday closing time
     * @param totalNumberOfSeats the number of seats of the restaurant
     * @param contactNumber the contact number of the restaurant
     * @param email the email of the restaurant
     * @return true if update operation is completed
     * @throws ParseException
     * @throws ClassNotFoundException
     * @throws SQLException 
     */
    public boolean update(String monToFryOt,String monToFryCt,String satOt,String satCt,String sunOt,String sunCt,
                          int totalNumberOfSeats,String contactNumber,String email) throws ParseException, ClassNotFoundException, SQLException{
        DateFormat formatter = new SimpleDateFormat("HH:mm");
        Date MonToFryOpeningTime = formatter.parse(monToFryOt);
        Date MonToFryclosingTime = formatter.parse(monToFryCt);
        Date satOpeningTime = formatter.parse(satOt);
        Date satclosingTime = formatter.parse(satCt);
        Date sunOpeningTime = formatter.parse(sunOt);
        Date sunClosingTime = formatter.parse(sunCt);
        
        RestaurantModel resModel = RestaurantModel.getInstance();
        
        if(MonToFryOpeningTime.after(MonToFryclosingTime) || satOpeningTime.after(satclosingTime) 
                || sunOpeningTime.after(sunClosingTime)){
           
            return false;
            
        }
        resModel.setMonFriOpTime(MonToFryOpeningTime);
        resModel.setMonFriClTime(MonToFryclosingTime);
        resModel.setSatOpTime(satOpeningTime);
        resModel.setSatClTime(satclosingTime);
        resModel.setSunOpTime(sunOpeningTime);
        resModel.setSunClTime(sunClosingTime);
        
        if(totalNumberOfSeats <= 0){
           return false;
        }
        
        resModel.setTotalNumberOfSeats(totalNumberOfSeats);
        resModel.setContactNumber(contactNumber);
        resModel.setEmail(email);
        resModel.update();
        return true;
    }
    
    /**
     * creates a restaurant account into the db
     * @param email the email of the restaurant
     * @param password the password of the restaurant
     * @param restaurantName the restaurant name
     * @param addressLine1 the address of the restaurant
     * @param area the area where the restaurant is situated
     * @param postCode the post code of the restaurant
     * @param contactNumber the contact number of the restaurant 
     * @param foodType the food type the restaurant sells
     * @param totalNumberOfSeats the total number of seats of the restaurant
     * @return true if the data is correct
     * @throws ClassNotFoundException
     * @throws SQLException 
     */
    public boolean signup(String email,String password,String restaurantName,String addressLine1,
            String area,String postCode,String contactNumber,String foodType,int totalNumberOfSeats)
            throws ClassNotFoundException, SQLException{
        if(!Validator.validateEmail(email)) return false;
        RestaurantModel resModel = RestaurantModel.getInstance();
        resModel.setEmail(email);
        resModel.setPassword(password);
        resModel.setName(restaurantName);
        resModel.setAddressLine1(addressLine1);
        resModel.setArea(area);
        resModel.setPostCode(postCode);
        resModel.setContactNumber(contactNumber);
        resModel.setFoodType(foodType);
        
        if(totalNumberOfSeats <= 0){
            return false;
        }
        resModel.setTotalNumberOfSeats(totalNumberOfSeats);
        resModel.insert();
        return true;
    }
    
    /**
     * permit a restaurant to login
     * @param password the password inserted by the restaurant user
     * @param email the email inserted by the restaurant user
     * @return true if the operations is concluded without errors
     * @throws ClassNotFoundException
     * @throws SQLException 
     */
    public boolean login(String password,String email) throws ClassNotFoundException, SQLException{
        RestaurantModel resModel = RestaurantModel.getInstance();
        return resModel.isPresentAccountIntoDb(email,password);
    }
    
    /**
     * 
     * @param bookedSeats the booked seats field to be updated
     * @param email the email of the restaurant 
     * @return true if the operations is concluded without errors
     * @throws ClassNotFoundException
     * @throws SQLException 
     */
    public boolean updateNumberOfSeats(int bookedSeats,String email) throws ClassNotFoundException, SQLException{
        if(bookedSeats <= 0){
            return false;
        }
        else{
            RestaurantModel resModel = RestaurantModel.getInstance();
            resModel.setBookedSeats(bookedSeats);
            resModel.setEmail(email);
            resModel.updateNumberOfSeats();
            return true;
        }
    }

}
