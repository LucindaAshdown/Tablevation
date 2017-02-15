/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import java.io.IOException;
import java.sql.SQLException;
import java.util.LinkedList;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author benha
 */
@WebServlet(name = "UserController", urlPatterns = {"/UserController"})
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
        } else if ("select_restaurants_by_area".equals(action)) {
            HttpSession sess = request.getSession();
            String email = (String) sess.getAttribute("email");
            String typeOfUser = (String) sess.getAttribute("type_of_user");
            if (email != null && typeOfUser != null) {
                String restaurantAreas = request.getParameter("Area");
                try {
                    RestaurantModel resModel = RestaurantModel.getInstance();
                    LinkedList<RestaurantModel> restaurantList = resModel.selectByArea(restaurantAreas);
                    request.setAttribute("restaurantList", restaurantList);
                    RequestDispatcher view = request.getRequestDispatcher("");
                    view.forward(request, response);
                } catch (Exception e) {

                }
            }
        }

    }

    public boolean login(String password, String email) throws ClassNotFoundException, SQLException {
        CustomerModel cusModel = CustomerModel.getInstance();
        return cusModel.isPresentAccountIntoDb(email, password);
    }
}
