/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.SQLException;
import java.util.Random;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Nota
 */
public class CustomerModelTest {

    private String email;
    private String password;
    
    public CustomerModelTest(){
        Random rn = new Random();
        int random = rn.nextInt(1000) + 1;
        int random1 = rn.nextInt(1000) + 1;
        this.email = random + "@" + random1 + ".com";
        this.password = "Francesco1";
    }
    
    /**
     * Test of getInstance method, of class CustomerModel.
     * the test checks that after a customer object model has been created
     * with this method calling it again will result in having the same reference
     * @throws java.lang.Exception
     */
    @Test
    public void testGetInstance() throws Exception {
        CustomerModel cs = CustomerModel.getInstance();
        CustomerModel cs1 = CustomerModel.getInstance();
        assertEquals(cs,cs1);
    }

    /**
     * Test of insert method, of class CustomerModel.
     */
    @Test
    public void testInsert() throws ClassNotFoundException {
        try{
            CustomerModel cs = CustomerModel.getInstance();
            cs.setEmail(this.email);
            cs.setPassword(this.password);
            cs.setForename("Francesco David");
            cs.setSurname("Nota");
            cs.setContactNumber("081924535");
            
            cs.insert();
        } catch (SQLException ex) {
            fail("failure while inserting a restaurant new account into the DB\n");
        }
    }

    /**
     * Test of update method, of class CustomerModel.
     */
    @Test
    public void testUpdate() throws ClassNotFoundException{
        try{
            CustomerModel cs = CustomerModel.getInstance();
            
            cs.setForename("Lucinda");
            cs.setSurname("Ash");
            cs.setContactNumber("089999999");
            cs.setEmail("nota@nota.com");
            
            cs.update();
        } catch (SQLException ex) {
            fail("failure while updating a restaurant account into the DB\n");
        }
    }

    /**
     * Test of isPresentAccountIntoDb method, of class CustomerModel.
     */
    @Test
    public void testIsPresentAccountIntoDb() throws Exception {
        CustomerModel cs = CustomerModel.getInstance();
        assertTrue(cs.isPresentAccountIntoDb("nota@nota.com", "Francesco1"));
    }

    /**
     * Test of getEmail method, of class CustomerModel.
     */
    @Test
    public void testGetAndSetEmail() throws ClassNotFoundException, SQLException {
        CustomerModel cs = CustomerModel.getInstance();
        cs.setEmail("fra@fra.com");
        assertEquals("fra@fra.com", cs.getEmail());
    }

    /**
     * Test of getPassword method, of class CustomerModel.
     */
    @Test
    public void testGetAndSetPassword() throws ClassNotFoundException, SQLException {
        CustomerModel cs = CustomerModel.getInstance();
        cs.setPassword("francesco1");
        assertEquals("francesco1", cs.getPassword());
    }


    /**
     * Test of getForename method, of class CustomerModel.
     */
    @Test
    public void testGetAndSetForename() throws ClassNotFoundException, SQLException {
        CustomerModel cs = CustomerModel.getInstance();
        cs.setForename("francesco");
        assertEquals("francesco", cs.getForename());
    }

    /**
     * Test of getSurname method, of class CustomerModel.
     */
    @Test
    public void testGetAndSetSurname() throws ClassNotFoundException, SQLException {
        CustomerModel cs = CustomerModel.getInstance();
        cs.setSurname("francesco");
        assertEquals("francesco", cs.getSurname());
    }

    /**
     * Test of setContactNumber method, of class CustomerModel.
     */
    @Test
    public void testGetAndSetContactNumber() throws ClassNotFoundException, SQLException {
        CustomerModel cs = CustomerModel.getInstance();
        cs.setContactNumber("3536567654");
        assertEquals("3536567654", cs.getContactNumber());
    }
}
