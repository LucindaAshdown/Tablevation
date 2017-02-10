/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Time;
import java.util.Date;
import java.util.LinkedList;

/**
 * A class that manages Restaurant data
 * and execute queries on the database
 * @author Francesco David Nota
 */
public class RestaurantModel implements Model{
    
    private final Connection conn;
    private String email;
    private String password;
    private String name;
    private String addressLine1;
    private String area;
    private String city;
    private String county;
    private String postCode;
    private int rating;
    private int bookedSeats;
    private String foodType;
    private int totalNumberOfSeats;
    private String contactNumber;
    private Date monFriOpTime;
    private Date monFriClTime;
    private Date satOpTime;
    private Date satClTime;
    private Date sunOpTime;
    private Date sunClTime;
    
    private static RestaurantModel restaurantModel = null;
    
    /**
     * constructor
     * @throws ClassNotFoundException
     * @throws SQLException
     */
    private RestaurantModel() throws ClassNotFoundException, SQLException{
       conn = Database.getConnection();
    }
    
    public static RestaurantModel getInstance() throws SQLException, ClassNotFoundException{
       if(restaurantModel == null)
           restaurantModel = new RestaurantModel();
       return restaurantModel;
    }
    
    // METHODS INTERFACING WITH THE DATABASE //
    
    @Override
    public void insert() {
        String query = "INSERT INTO Restaurant "
                + "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
        try {
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setString(1, this.email);
            ps.setString(2, this.password);
            ps.setString(3, this.name); /*name */
            ps.setString(4, this.addressLine1); /*Address line 1 */
            ps.setString(5, this.area); /*Area */
            ps.setString(6, "Portsmouth"); /*City */
            ps.setString(7, "Hampshire"); /*County */
            ps.setString(8, this.postCode); /*PostCode */
            ps.setInt(9, -1); /*Rating */
            ps.setInt(10, -1);
            ps.setString(11, this.contactNumber); /*Contact Number */
            Time currentTime = new Time((new Date()).getTime());
            ps.setTime(12, new Time(currentTime.getTime())); /* Monday to Friday Opening */
            ps.setTime(13, new Time(currentTime.getTime())); /* Monday to Friday Closing */ /* Monday to Friday Opening */
            ps.setTime(14, new Time(currentTime.getTime()));
            ps.setTime(15, new Time(currentTime.getTime())); /* Saturday Closing Time */
            ps.setTime(16, new Time(currentTime.getTime())); /* Sunday Opening Time */
            ps.setTime(17, new Time(currentTime.getTime())); /* Sunday Closing Time */
            ps.setString(18, this.foodType);
            ps.setInt(19, this.totalNumberOfSeats);
            
            ps.executeUpdate();
            
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        
    }

    @Override
    public void update() {
        String query = "UPDATE Restaruant SET (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) WHERE Restaurant.email = ?";
            try {
                PreparedStatement ps = conn.prepareStatement(query);
                ps.setString(1, this.name); /*name */
                ps.setString(2, this.addressLine1); /*Address line 1 */
                ps.setString(3, this.area); /*Area */
                ps.setString(4, this.city); /*City */
                ps.setString(5, this.county); /*County */
                ps.setString(6, this.postCode); /*PostCode */
                ps.setInt(7, this.rating); /*Rating */
                ps.setString(8, this.contactNumber); /*Contact Number */
                Date currentDate = new Date();
                Time currentTime = new Time(currentDate.getTime());
                ps.setTime(9, new Time(this.monFriOpTime.getTime())); /* Monday to Friday Opening */
                ps.setTime(10, new Time(this.monFriClTime.getTime())); /* Monday to Friday Closing */ /* Monday to Friday Opening */
                ps.setTime(11, new Time(this.satOpTime.getTime()));
                ps.setTime(12, new Time(this.satClTime.getTime())); /* Saturday Closing Time */
                ps.setTime(13, new Time(this.sunOpTime.getTime())); /* Sunday Opening Time */
                ps.setTime(14, new Time(this.sunClTime.getTime())); /* Sunday Closing Time */
                ps.setString(15, this.foodType);
                ps.setInt(16, this.totalNumberOfSeats);
                
                ps.setString(17, this.email); /* where statement email */
                
                ps.executeUpdate();
                conn.commit();
            
        } catch (SQLException ex) {
            
        }
        
    }

    @Override
    public LinkedList<Object> select(LinkedList<Object> keys) {
        return null;
    }
    
    /**
     * @param area parameter used to find restaurants having has attribute the area
     * @return the list of restaurants belonging to the selected area
     */    
    public LinkedList<RestaurantModel> selectByArea(String area){
        return null;
    }
    
    /**
     * @param foodType parameter used to find restaurants having has attribute the area
     * @return the list of restaurants belonging to the selected area
     */  
    public LinkedList<RestaurantModel> selectByFoodType(String foodType){
        return null;    
    }
    
    // GETTERS AND SETTERS //
    
    /**
     * @return the email
     */
    public String getEmail() {
        return email;
    }

    /**
     * @param email the email to set
     */
    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * @return the password
     */
    public String getPassword() {
        return password;
    }

    /**
     * @param password the password to set
     */
    public void setPassword(String password) {
        this.password = password;
    }

    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @return the addressLine1
     */
    public String getAddressLine1() {
        return addressLine1;
    }

    /**
     * @param addressLine1 the addressLine1 to set
     */
    public void setAddressLine1(String addressLine1) {
        this.addressLine1 = addressLine1;
    }

    /**
     * @return the area
     */
    public String getArea() {
        return area;
    }

    /**
     * @param area the area to set
     */
    public void setArea(String area) {
        this.area = area;
    }

    /**
     * @return the city
     */
    public String getCity() {
        return city;
    }

    /**
     * @param city the city to set
     */
    public void setCity(String city) {
        this.city = city;
    }

    /**
     * @return the county
     */
    public String getCounty() {
        return county;
    }

    /**
     * @param county the county to set
     */
    public void setCounty(String county) {
        this.county = county;
    }

    /**
     * @return the postCode
     */
    public String getPostCode() {
        return postCode;
    }

    /**
     * @param postCode the postCode to set
     */
    public void setPostCode(String postCode) {
        this.postCode = postCode;
    }

    /**
     * @return the rating
     */
    public int getRating() {
        return rating;
    }

    /**
     * @param rating the rating to set
     */
    public void setRating(int rating) {
        this.rating = rating;
    }

    /**
     * @return the bookedSeats
     */
    public int getBookedSeats() {
        return bookedSeats;
    }

    /**
     * @param bookedSeats the bookedSeats to set
     */
    public void setBookedSeats(int bookedSeats) {
        this.bookedSeats = bookedSeats;
    }

    /**
     * @return the foodType
     */
    public String getFoodType() {
        return foodType;
    }

    /**
     * @param foodType the foodType to set
     */
    public void setFoodType(String foodType) {
        this.foodType = foodType;
    }

    /**
     * @return the totalNumberOfSeats
     */
    public int getTotalNumberOfSeats() {
        return totalNumberOfSeats;
    }

    /**
     * @param totalNumberOfSeats the totalNumberOfSeats to set
     */
    public void setTotalNumberOfSeats(int totalNumberOfSeats) {
        this.totalNumberOfSeats = totalNumberOfSeats;
    }

    /**
     * @return the contactNumber
     */
    public String getContactNumber() {
        return contactNumber;
    }

    /**
     * @param contactNumber the contactNumber to set
     */
    public void setContactNumber(String contactNumber) {
        this.contactNumber = contactNumber;
    }

    /**
     * @return the satOpTime
     */
    public Date getSatOpTime() {
        return satOpTime;
    }

    /**
     * @param satOpTime the satOpTime to set
     */
    public void setSatOpTime(Date satOpTime) {
        this.satOpTime = satOpTime;
    }

    /**
     * @return the satClTime
     */
    public Date getSatClTime() {
        return satClTime;
    }

    /**
     * @param satClTime the satClTime to set
     */
    public void setSatClTime(Date satClTime) {
        this.satClTime = satClTime;
    }

    /**
     * @return the sunOpTime
     */
    public Date getSunOpTime() {
        return sunOpTime;
    }

    /**
     * @param sunOpTime the sunOpTime to set
     */
    public void setSunOpTime(Date sunOpTime) {
        this.sunOpTime = sunOpTime;
    }

    /**
     * @return the sunClTime
     */
    public Date getSunClTime() {
        return sunClTime;
    }

    /**
     * @param sunClTime the sunClTime to set
     */
    public void setSunClTime(Date sunClTime) {
        this.sunClTime = sunClTime;
    }

}
