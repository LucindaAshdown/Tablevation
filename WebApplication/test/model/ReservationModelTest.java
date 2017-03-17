/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.SQLException;
import java.util.Date;
import java.util.LinkedList;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Nota
 */
public class ReservationModelTest {

    
    /**
     * Test of getInstance method, of class ReservationModel.
     */
    @Test
    public void testGetInstance() throws Exception {
        ReservationModel expResult = ReservationModel.getInstance();
        ReservationModel result = ReservationModel.getInstance();
        assertEquals(expResult, result);
    }

    /**
     * Test of insert method, of class ReservationModel.
     */
    @Test
    public void testInsert() throws ClassNotFoundException {
        ReservationModel reservation;
        try {
            reservation = ReservationModel.getInstance();
            reservation.setRestaurantName("Lucinda restaurant");
            reservation.setRestaurantEmail("luc@luc.com");
            reservation.setCustomerEmail("nota@nota.com");
            Date date = new Date();
            reservation.setBookedDate(date);
            reservation.setNumberOfGuests(5);
            reservation.setDetails("details string reservation example");
            reservation.insert();
        } catch (SQLException ex) {
            fail("failure while inserting a reservation into the DB\n");
        }
    }

    @Test
    public void testAlreadyBooked() throws ClassNotFoundException, SQLException{
       ReservationModel reservation = ReservationModel.getInstance();
       reservation.setRestaurantName("Lucinda restaurant");
       reservation.setRestaurantEmail("luc@luc.com");
       reservation.setCustomerEmail("nota@nota.com");
       Date date = new Date();
       reservation.setBookedDate(date);
       reservation.setNumberOfGuests(5);
       reservation.setDetails("details string reservation example");
       reservation.insert();
       
       assertTrue(reservation.alreadyBooked(date, "luc@luc.com"));
       assertEquals(false,reservation.alreadyBooked(date, "l@c.com"));
       
       Date d1 = new Date(date.getTime() + 60000000);
       assertEquals(false,reservation.alreadyBooked(date, "l@c.com"));
    }
    
    /**
     * Test of selectAllReservationByCustomerEmail method, of class ReservationModel.
     */
    @Test
    public void testSelectAllReservationByCustomerEmail() throws ClassNotFoundException {
        try {
            String email = "nota@nota.com";
            ReservationModel reservation = ReservationModel.getInstance();
            LinkedList<ReservationModel> result = reservation.selectAllReservationByCustomerEmail(email);
            
            int length = result.size();
            for(int i = 0;i < length;i++){
                assertEquals(email,result.get(i).getCustomerEmail());
            }
        } catch (SQLException ex) {
            fail("Error while selecting reservations by customer email");
        }
    }

    /**
     * Test of selectAllReservationByRestaurantEmail method, of class ReservationModel.
     */
    @Test
    public void testSelectAllReservationByRestaurantEmail() throws Exception {
        try {
            String email = "luc@luc.com";
            ReservationModel reservation = ReservationModel.getInstance();
            LinkedList<ReservationModel> result = reservation.selectAllReservationByRestaurantEmail(email);
            
            int length = result.size();
            for(int i = 0;i < length;i++){
                assertEquals(email,result.get(i).getRestaurantEmail());
            }
        } catch (SQLException ex) {
            fail("Error while selecting reservations by restaurant email");
        }
    }
}