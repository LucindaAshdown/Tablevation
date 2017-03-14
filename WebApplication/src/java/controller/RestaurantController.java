/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package controller;

import java.io.IOException;
import java.sql.SQLException;
import java.text.DateFormat;
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
                    RestaurantModel resModel = RestaurantModel.getInstance();
                    resModel.setEmail(email);
                    resModel.setPassword(password);
                    resModel.setName(restaurantName);
                    resModel.setAddressLine1(addressLine1);
                    resModel.setArea(area);
                    resModel.setPostCode(postCode);
                    resModel.setContactNumber(contactNumber);
                    resModel.setFoodType(foodType);
                    resModel.setTotalNumberOfSeats(totalNumberOfSeats);
                    resModel.insert();
                    
                    RequestDispatcher view = request.getRequestDispatcher("index.jsp");
                    view.forward(request, response);
                }
                catch(Exception e){
                    e.printStackTrace();
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
            
            DateFormat formatter = new SimpleDateFormat("HH:mm");
            
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
                    Date MonToFryOpeningTime = formatter.parse(monToFryOt);
                    Date MonToFryclosingTime = formatter.parse(monToFryCt);
                    Date satOpeningTime = formatter.parse(satOt);
                    Date satclosingTime = formatter.parse(satCt);
                    Date sunOpeningTime = formatter.parse(sunOt);
                    Date sunClosingTime = formatter.parse(sunCt);
                    
                    RestaurantModel resModel = RestaurantModel.getInstance();
                    resModel.setMonFriOpTime(MonToFryOpeningTime);
                    resModel.setMonFriClTime(MonToFryclosingTime);
                    resModel.setSatOpTime(satOpeningTime);
                    resModel.setSatClTime(satclosingTime);
                    resModel.setSunOpTime(sunOpeningTime);
                    resModel.setSunClTime(sunClosingTime);
                    resModel.setTotalNumberOfSeats(totalNumberOfSeats);
                    resModel.setContactNumber(contactNumber);
                    resModel.setEmail(email);
                    resModel.update();
                    RequestDispatcher view = request.getRequestDispatcher("RestaurantMenu.html");
                    view.forward(request, response);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        else if("update_number_of_seats".equals(action)){
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            int bookedSeats = Integer.parseInt(request.getParameter("Booked_seats"));
            if (email != null) {
                try {
                    RestaurantModel resModel = RestaurantModel.getInstance();
                    resModel.setBookedSeats(bookedSeats);
                    resModel.setEmail(email);
                    resModel.updateNumberOfSeats();
                    RequestDispatcher view = request.getRequestDispatcher("RestaurantMenu.html");
                    view.forward(request, response);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
    
    public boolean login(String password,String email) throws ClassNotFoundException, SQLException{
        RestaurantModel resModel = RestaurantModel.getInstance();
        return resModel.isPresentAccountIntoDb(email,password);
    }

}
