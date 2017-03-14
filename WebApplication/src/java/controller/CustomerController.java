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
import model.CustomerModel;
import model.ReservationModel;
import model.RestaurantModel;

/**
 *
 * @author benha
 */
@WebServlet(name = "CustomerController", urlPatterns = {"/CustomerController"})
public class CustomerController extends HttpServlet {
    
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
        if ("sign_up".equals(action)) {
            String email = request.getParameter("Customer_Email");
            String password = request.getParameter("Customer_Password");
            String forename = request.getParameter("Forename");
            String surname = request.getParameter("Surname");
            String contactNumber = request.getParameter("Contact_Number");
            
            if (email != null && password != null && surname != null && forename != null && contactNumber != null) {
                try {
                    CustomerModel cusModel = CustomerModel.getInstance();
                    cusModel.setEmail(email);
                    cusModel.setPassword(password);
                    cusModel.setForename(forename);
                    cusModel.setSurname(surname);
                    cusModel.setContactNumber(contactNumber);
                    
                    cusModel.insert();
                    RequestDispatcher view = request.getRequestDispatcher("index.jsp");
                    view.forward(request, response);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        else if ("select_restaurants_by_area".equals(action)) {
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            String typeOfUser = (String) sess.getAttribute("type_of_user");
            if (email != null && typeOfUser != null) {
                String restaurantArea = request.getParameter("Area").toLowerCase();
                try {
                    RestaurantModel resModel = RestaurantModel.getInstance();
                    LinkedList<RestaurantModel> restaurantList = resModel.selectByArea(restaurantArea);
                    request.setAttribute("restaurantList", restaurantList);
                    RequestDispatcher view = request.getRequestDispatcher("CustomerSearchRestaurants.jsp");
                    view.forward(request, response);
                } catch (Exception e) {
                    
                }
            }
        }
        else if("select_reservations".equals(action)){
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            String typeOfUser = (String) sess.getAttribute("type_of_user");
            if (email != null && typeOfUser != null) {
                try {
                    ReservationModel resModel = ReservationModel.getInstance();
                    LinkedList<ReservationModel> reservationList = resModel.selectAllReservationByCustomerEmail(email);
                    request.setAttribute("reservationList", reservationList);
                    RequestDispatcher view = request.getRequestDispatcher("CustomerViewReservations.jsp");
                    view.forward(request, response);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        else if("reservation_page".equals(action)){
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            String typeOfUser = (String) sess.getAttribute("type_of_user");
            if (email != null && typeOfUser != null) {
                RequestDispatcher view = request.getRequestDispatcher("CustomerMakeBooking.jsp");
                view.forward(request, response);
            }
        }
        else if("make_reservation".equals(action)){
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            String typeOfUser = (String) sess.getAttribute("type_of_user");
            if (email != null && typeOfUser != null) {
                String bookedDate = request.getParameter("Booked_Date");
                String bookedTime = request.getParameter("Booked_Time");
                int numberOfGuests = Integer.parseInt(request.getParameter("No_Guests"));
                String restaurantEmail = request.getParameter("Restaurant_Email");
                String name = request.getParameter("Restaurant_Name");
                String details = request.getParameter("Details");
                
                DateFormat formatter = new SimpleDateFormat("MM/dd/yy HH:mm");
                try {
                    Date date = formatter.parse(bookedDate + " " + bookedTime);
                    ReservationModel reservationModel = ReservationModel.getInstance();
                    reservationModel.setNumberOfGuests(numberOfGuests);
                    reservationModel.setRestaurantEmail(restaurantEmail);
                    reservationModel.setCustomerEmail(email);
                    reservationModel.setBookedDate(date);
                    reservationModel.setRestaurantName(name);
                    reservationModel.setDetails(details);
                    
                    reservationModel.insert();
                    RequestDispatcher view = request.getRequestDispatcher("CustomerMenu.jsp");
                    view.forward(request, response);
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
        }
        else if("update".equals(action)){
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            if (email != null) {
                String forename = request.getParameter("Forename");
                String surname = request.getParameter("Surname");
                String contactNumber = request.getParameter("Contact_Number");
                
                if (surname != null && forename != null && contactNumber != null) {
                    try {
                        CustomerModel cusModel = CustomerModel.getInstance();
                        cusModel.setForename(forename);
                        cusModel.setSurname(surname);
                        cusModel.setContactNumber(contactNumber);
                        cusModel.setEmail(email);
                        
                        cusModel.update();
                        RequestDispatcher view = request.getRequestDispatcher("CustomerMenu.jsp");
                        view.forward(request, response);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
    
    
    public boolean login(String password, String email) throws ClassNotFoundException, SQLException {
        CustomerModel cusModel = CustomerModel.getInstance();
        return cusModel.isPresentAccountIntoDb(email, password);
    }
}
