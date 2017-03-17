/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import java.sql.SQLException;
import java.util.Date;
import java.util.Random;
import model.ReservationModel;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Nota
 */
public class CustomerControllerTest {

    private CustomerController cs;
    private String email;
    
    public CustomerControllerTest(){
        this.cs = new CustomerController();
        Random rn = new Random();
        int random = rn.nextInt(1000) + 1;
        int random1 = rn.nextInt(1000) + 1;
        this.email = random + "@" + random1 + ".com";
    }
    /**
     * Test of login method, of class CustomerController.
     */
    @Test
    public void testLogin() throws Exception {
        String password = "Francesco1";
        String email = "nota@nota.com";
        CustomerController instance = new CustomerController();
        boolean expResult = true;
        boolean result = instance.login(password, email);
        assertEquals(expResult, result);
        
        email = "na@nta.com";
        password = "Fraco1";
        expResult = false;
        result = instance.login(password, email);
        assertEquals(expResult, result);  
    }
    
    public void testSignup() throws ClassNotFoundException, SQLException{
        String password = "osuhr";
        String forename = "Julia";
        String surname = "sugar";
        String contactNumber = "0934567890";
        
        assertTrue(cs.signup(this.email, password, forename, surname, contactNumber));
        
        String notValidEmail = "gsioun";
        assertEquals(false,cs.signup(notValidEmail, password, forename, surname, contactNumber));
    }
    
    public void testMakeReservation() throws ClassNotFoundException, SQLException{
        int numberOfGuests = 4;
        String restaurantEmail = "luc@luc.com";
        String email = "nota@nota.com";
        Date currentDate = new Date();
        Date testDate = new Date(currentDate.getTime() + 60000000);
        String name = "isrgsgr";
        String details = "datails";
        ReservationModel rs = ReservationModel.getInstance();
        assertEquals(true,cs.makeReservation(rs, numberOfGuests, restaurantEmail, email, testDate, name, details));
        
        numberOfGuests = 0;
        assertEquals(false,cs.makeReservation(rs, numberOfGuests, restaurantEmail, email, testDate, name, details));
        numberOfGuests = 5;
        
        testDate = new Date(currentDate.getTime() - 60000000);
        assertEquals(false,cs.makeReservation(rs, numberOfGuests, restaurantEmail, email, testDate, name, details));
    }
}
