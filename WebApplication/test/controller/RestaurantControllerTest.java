/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import java.sql.SQLException;
import java.text.ParseException;
import java.util.Random;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Nota
 */
public class RestaurantControllerTest {
    private RestaurantController rs;
    private String email;
            
    public RestaurantControllerTest(){
        rs = new RestaurantController();
        Random rn = new Random();
        int random = rn.nextInt(1000) + 1;
        int random1 = rn.nextInt(1000) + 1;
        this.email = random + "@" + random1 + ".com";
    }
    /**
     * Test of login method, of class RestaurantController.
     */
    @Test
    public void testLogin() throws Exception {
        String password = "Lucinda1";
        String email = "luc@luc.com";
        boolean expResult = true;
        boolean result = rs.login(password, email);
        assertEquals(expResult, result);
        
        email = "na@nta.com";
        password = "Fraco1";
        expResult = false;
        result = rs.login(password, email);
        assertEquals(expResult, result);
    }
    
    @Test
    public void testSignup() throws ClassNotFoundException, SQLException{
        String password = "Francesco3553";
        String restaurantName = "Jamie Rest";
        String addressLine1 = "example street";
        String area = "southsea";
        String postCode = "COD DFFD";
        String contactNumber = "04444028592";
        String foodType = "indian";
        int numberOfSeats = 20;
        assertTrue(rs.signup(this.email, password, restaurantName, addressLine1, area, postCode, contactNumber, foodType, numberOfSeats));
        
        assertEquals(false,rs.signup(this.email, password, restaurantName, addressLine1, area, postCode, contactNumber, foodType, 0));
        assertEquals(false,rs.signup(this.email, password, restaurantName, addressLine1, area, postCode, contactNumber, foodType, -5));
        
        email = "aoeugn";
        assertEquals(false,rs.signup(email, password, restaurantName, addressLine1, area, postCode, contactNumber, foodType, numberOfSeats));
    }
    
    @Test
    public void testUpdate() throws ParseException, ClassNotFoundException, SQLException{
        String monToFryOt = "10:20";
        String monToFryCt = "12:30";
        String satOt = "11:40";
        String satCt = "12:20";
        String sunOt = "11:20";
        String sunCt = "15:20";
        int totalNumberOfSeats = 2;
        String contactNumber = "2535902503";
        String email = "na@na.com";
        
        assertTrue(rs.update(monToFryOt, monToFryCt, satOt, satCt, sunOt, sunCt, totalNumberOfSeats, contactNumber, email));
        
        monToFryOt = "12:31";
        assertEquals(false,rs.update(monToFryOt, monToFryCt, satOt, satCt, sunOt, sunCt, totalNumberOfSeats, contactNumber, email));
        monToFryOt = "10:30";
        
        satOt = "12:21";
        assertEquals(false,rs.update(monToFryOt, monToFryCt, satOt, satCt, sunOt, sunCt, totalNumberOfSeats, contactNumber, email));
        satOt = "11:40";
        
        sunOt = "15:21";
        assertEquals(false,rs.update(monToFryOt, monToFryCt, satOt, satCt, sunOt, sunCt, totalNumberOfSeats, contactNumber, email));
        sunOt = "11:20";
        
        totalNumberOfSeats = 0;
        assertEquals(false,rs.update(monToFryOt, monToFryCt, satOt, satCt, sunOt, sunCt, totalNumberOfSeats, contactNumber, email));
    
        totalNumberOfSeats = -5;
        assertEquals(false,rs.update(monToFryOt, monToFryCt, satOt, satCt, sunOt, sunCt, totalNumberOfSeats, contactNumber, email));
    }
    
    @Test
    public void testUpdateNumberOfBookedSeats() throws ClassNotFoundException, SQLException{
        String email = "luc@luc.com";
        int bookedSeats = 20;
        
        assertTrue(rs.updateNumberOfSeats(bookedSeats, email));
        assertEquals(false,rs.updateNumberOfSeats(0, email));
        assertEquals(false,rs.updateNumberOfSeats(-15, email));
    }
}