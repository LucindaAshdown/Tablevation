/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import java.io.IOException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author Nota
 */
@WebServlet(name = "Controller", urlPatterns = {"/Controller"})
public class Controller extends HttpServlet {
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
        if("login".equals(action)){
           String email = request.getParameter("email");
           String password = request.getParameter("password");
           String typeOfUser = request.getParameter("type_of_user");
           try{
               boolean loggedIn;
               if(typeOfUser.equals("customer")){
                   CustomerController customerController = new CustomerController();
                   loggedIn = customerController.login(password, email);
               }
               else{
                   RestaurantController restaurantController = new RestaurantController();
                   loggedIn = restaurantController.login(password, email);
               }
               if(loggedIn){
                   HttpSession session = request.getSession();
                   session.setAttribute("email", email);
                   session.setAttribute("type_of_user", typeOfUser);
                   RequestDispatcher view = request.getRequestDispatcher("index.jsp");
                   view.forward(request, response);
               }
           }
           catch(Exception e){
               e.printStackTrace();
           }
        }
        else if("logout".equals(action)){
            HttpSession sess = request.getSession();
            sess.removeAttribute("email");
            sess.removeAttribute("type_of_user");
            RequestDispatcher view = request.getRequestDispatcher("index.jsp");
            view.forward(request, response);
        }
    }

}
