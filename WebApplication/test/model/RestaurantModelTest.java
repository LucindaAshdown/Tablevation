/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.SQLException;
import java.util.Date;
import java.util.LinkedList;
import java.util.Random;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Nota
 */
public class RestaurantModelTest {
    
    private String email;
    private String password;
    
    public RestaurantModelTest(){
        Random rn = new Random();
        int random = rn.nextInt(1000) + 1;
        int random1 = rn.nextInt(1000) + 1;
        this.email = random + "@" + random1 + ".com";
        this.password = "Jamie1";
    }

    /**
     * Test of getInstance method, of class RestaurantModel.
     */
    @Test
    public void testGetInstance() throws Exception {
        RestaurantModel expResult = RestaurantModel.getInstance();
        RestaurantModel result = RestaurantModel.getInstance();
        assertEquals(expResult, result);
    }

    /**
     * Test of insert method, of class RestaurantModel.
     */
    @Test
    public void testInsert() throws ClassNotFoundException {
        try{
            RestaurantModel rest = RestaurantModel.getInstance();
            rest.setEmail(this.email);
            rest.setPassword(this.password);
            rest.setName("Jamie restaurant");
            rest.setAddressLine1("jamie street");
            rest.setArea("southsea");
            rest.setCity("Portsmouth");
            rest.setCounty("Hampshire");
            rest.setPostCode("");
            rest.setRating(-1);
            rest.setBookedSeats(0);
            rest.setContactNumber("0986545678");
            rest.setFoodType("italian");
            rest.setTotalNumberOfSeats(20);
            
            Date currentDate = new Date();
            rest.setMonFriOpTime(currentDate);
            Date closingTime = new Date(currentDate.getTime() + 6000000);
            rest.setMonFriClTime(closingTime);
            rest.setSatOpTime(currentDate);
            rest.setSatClTime(closingTime);
            rest.setSunOpTime(currentDate);
            rest.setSunClTime(closingTime);
            
            rest.insert();
        }
        catch(SQLException e){
            fail("fail while inserting a restaurant account");
        }
    }

    /**
     * Test of update method, of class RestaurantModel.
     */
    @Test
    public void testUpdate() throws ClassNotFoundException {
        try{

            RestaurantModel rest = RestaurantModel.getInstance();
            rest.setEmail(this.email);
            rest.setContactNumber("0986545678");
            rest.setTotalNumberOfSeats(25);
            
            Date currentDate = new Date();
            rest.setMonFriOpTime(currentDate);
            Date closingTime = new Date(currentDate.getTime() + 5000000);
            rest.setMonFriClTime(closingTime);
            rest.setSatOpTime(currentDate);
            rest.setSatClTime(closingTime);
            rest.setSunOpTime(currentDate);
            rest.setSunClTime(closingTime);
            
            rest.update();
        }
        catch(SQLException e){
            fail("fail while updating a restaurant account");
        }
    }

    /**
     * Test of updateNumberOfSeats method, of class RestaurantModel.
     */
    @Test
    public void testUpdateNumberOfSeats() throws ClassNotFoundException {
        try{
            RestaurantModel rest = RestaurantModel.getInstance();
            rest.setEmail(this.email);
            rest.setBookedSeats(10);
            
            rest.updateNumberOfSeats();
        }
        catch(SQLException e){
            fail("fail while updating the booked seats in the restaurant");
        }
    }

    /**
     * Test of isPresentAccountIntoDb method, of class RestaurantModel.
     */
    @Test
    public void testIsPresentAccountIntoDb() throws Exception {
        RestaurantModel rest = RestaurantModel.getInstance();
        boolean result = rest.isPresentAccountIntoDb("luc@luc.com", "Lucinda1");
        assertEquals(true,result);
        assertEquals(false,rest.isPresentAccountIntoDb("kacj@kaf.com", "vrbsh"));
    }

    /**
     * Test of selectByArea method, of class RestaurantModel.
     */
    @Test
    public void testSelectByArea() throws ClassNotFoundException{
        try {
            String area = "southsea";
            RestaurantModel rest = RestaurantModel.getInstance();
            LinkedList<RestaurantModel> restList = rest.selectByArea(area);
            
            String notExistingArea = "random string";
            LinkedList<RestaurantModel> restList1 = rest.selectByArea(notExistingArea);
            
            assertEquals(0,restList1.size());
        }
        catch (SQLException ex) {
            fail("fail while selecting restaurants by area");
        }
    }
}