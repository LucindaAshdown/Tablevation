/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package controller;

import java.io.IOException;
import java.sql.SQLException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
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
            String area = request.getParameter("Area");
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
    }
    
    public boolean login(String password,String email) throws ClassNotFoundException, SQLException{
        RestaurantModel resModel = RestaurantModel.getInstance();
        return resModel.isPresentAccountIntoDb(email,password);
    }

}
