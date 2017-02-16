/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.util.Date;
import java.util.LinkedList;

/**
 * @author Francesco David Nota
 */
public class ReservationModel implements Model{
    
    private Connection conn;
    private int id;
    private String restaurantName;
    private String restaurantEmail;
    private String customerEmail;
    private Date bookedDate;
    private int numberOfGuests;
    private String details;
    private static ReservationModel reservationModel = null;
    
    /**
     * constructor
     * @throws ClassNotFoundException
     * @throws SQLException
     */
    private ReservationModel(){}
    
    public static ReservationModel getInstance() throws ClassNotFoundException, SQLException{
         if(reservationModel == null){
             reservationModel = new ReservationModel();
             reservationModel.conn = Database.getConnection();
         }
         return reservationModel;
    }
    
    // METHODS INTERFACING WITH THE DATABASE //
    
    @Override
    public void insert() {
        String query = "INSERT INTO Reservation (Restaurant_Name,Restaurant_Email,Customer_Email,Booked_Date,No_Guests,Details)"
                + " VALUES (?,?,?,?,?,?)";
        try{
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setString(1, this.restaurantName);
            ps.setString(2, this.restaurantEmail);
            ps.setString(3, this.customerEmail);
            Timestamp bookedDate = new Timestamp(this.bookedDate.getTime());
            ps.setTimestamp(4, bookedDate);
            ps.setInt(5, this.numberOfGuests);
            ps.setString(6, this.details);
            
            ps.executeUpdate();
        }
        catch(Exception e){
            
        }
    }

    @Override
    public void update() {
        PreparedStatement ps;
        String query = "UPDATE Reservation SET (?,?,?,?)";
    }
    
    /**
     * @param email the unique email of the customer who wants to see the
     * reservations he made
     * @return the list of reservations made by the customer
     * @throws java.sql.SQLException
     */
    public LinkedList<ReservationModel> selectAllReservationByCustomerEmail(String email) throws SQLException{
        String query = "SELECT Restaurant_Name,Restaurant_Email,Customer_Email,Booked_Date,No_Guests,Details FROM Reservation "
                + "WHERE Customer_Email=?";
        return selectReservationsByEmail(email,query);
    }
    
    /**
     * @param email the unique email of the restaurant who wants to see the
     * reservations made by customers
     * @return the list of reservations received by a restaurant
     * @throws java.sql.SQLException
     */
    public LinkedList<ReservationModel> selectAllReservationByRestaurantEmail(String email) throws SQLException{
        String query = "SELECT Restaurant_Name,Restaurant_Email,Customer_Email,Booked_Date,No_Guests,Details FROM Reservation "
                + "WHERE Restaurant_Email=?";
       return selectReservationsByEmail(email,query);
    }
    
    
    private LinkedList<ReservationModel> selectReservationsByEmail(String email,String query) throws SQLException{
        PreparedStatement ps = conn.prepareStatement(query);
        ps.setString(1, email);
        ResultSet rs = ps.executeQuery();
        // if the result set is not empty it returns true
        LinkedList<ReservationModel> reservationModelList = new LinkedList<>();
        while(rs.next()){
           ReservationModel reservation = new ReservationModel();
           reservation.restaurantName = rs.getString(1);
           reservation.restaurantEmail = rs.getString(2);
           reservation.customerEmail = rs.getString(3);
           Timestamp bkDate = rs.getTimestamp(4);
           reservation.bookedDate = new Date(bkDate.getTime());
           reservation.numberOfGuests = rs.getInt(5);
           reservation.details = rs.getString(6);
           
           reservationModelList.add(reservation);
        }
        return reservationModelList;
    }
    
    // GETTERS AND SETTERS //
    
    /**
     * @return the id
     */
    public int getId() {
        return id;
    }

    /**
     * @param id the id to set
     */
    public void setId(int id) {
        this.id = id;
    }

    /**
     * @return the restaurantName
     */
    public String getRestaurantName() {
        return restaurantName;
    }

    /**
     * @param restaurantName the restaurantName to set
     */
    public void setRestaurantName(String restaurantName) {
        this.restaurantName = restaurantName;
    }

    /**
     * @return the restaurantEmail
     */
    public String getRestaurantEmail() {
        return restaurantEmail;
    }

    /**
     * @param restaurantEmail the restaurantEmail to set
     */
    public void setRestaurantEmail(String restaurantEmail) {
        this.restaurantEmail = restaurantEmail;
    }

    /**
     * @return the customerEmail
     */
    public String getCustomerEmail() {
        return customerEmail;
    }

    /**
     * @param customerEmail the customerEmail to set
     */
    public void setCustomerEmail(String customerEmail) {
        this.customerEmail = customerEmail;
    }

    /**
     * @return the bookedTime
     */
    public Date getBookedDate() {
        return bookedDate;
    }

    /**
     * @param bookedDate the bookedTime to set
     */
    public void setBookedDate(Date bookedDate) {
        this.bookedDate = bookedDate;
    }

    /**
     * @return the numberOfGuests
     */
    public int getNumberOfGuests() {
        return numberOfGuests;
    }

    /**
     * @param numberOfGuests the numberOfGuests to set
     */
    public void setNumberOfGuests(int numberOfGuests) {
        this.numberOfGuests = numberOfGuests;
    }

    /**
     * @return the details
     */
    public String getDetails() {
        return details;
    }

    /**
     * @param details the details to set
     */
    public void setDetails(String details) {
        this.details = details;
    }
    
    
}
