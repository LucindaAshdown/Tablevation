/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.LinkedList;

/**
 *
 * @author Francesco David Nota
 */
public class CustomerModel implements Model{

    private Connection conn;
    private String email;
    private String password;
    private String forename;
    private String surname;
    private String contactNumber;
    private static CustomerModel customerModel = null;
    
    /**
     * constructor
     * @throws ClassNotFoundException
     * @throws SQLException
     */
    private CustomerModel() throws ClassNotFoundException, SQLException{
       conn = Database.getConnection();
    }
    
    public static CustomerModel getInstance() throws ClassNotFoundException, SQLException{
         if(getCustomerModel() == null)
             setCustomerModel(new CustomerModel());
         return getCustomerModel();
    }
    
    @Override
    public void insert() {
        String query = "INSERT INTO Customer VALUES (?,?,?,?,?)";
        try{
            PreparedStatement ps = getConn().prepareStatement(query);
            ps.setString(1, this.getEmail());
            ps.setString(2, this.getPassword());
            ps.setString(3, this.getForename());
            ps.setString(4, this.getSurname());
            ps.setString(5, this.getContactNumber());
            
            ps.executeUpdate();
        }catch(SQLException ex){
            ex.printStackTrace();
        }
    }

    @Override
    public void update() {
        String query = "UPDATE Customer SET (?,?,?) WHERE Customer.email = ?";
        try{
            PreparedStatement ps = getConn().prepareStatement(query);
            ps.setString(1, this.getPassword());
            ps.setString(2, this.getForename());
            ps.setString(3, this.getSurname());
            ps.setString(4, this.getEmail());
            
            ps.executeUpdate();
        }catch(SQLException ex){
            ex.printStackTrace();
        }
    }
    
    public boolean isPresentAccountIntoDb(String email,String password) throws SQLException{
           String query = "SELECT Customer_email,Customer_password FROM Customer WHERE Customer_email=? AND Customer_password=?";
           PreparedStatement ps = getConn().prepareStatement(query);
           ps.setString(1, email);
           ps.setString(2, password);
           ResultSet rs = ps.executeQuery();
           // if the result set is not empty it returns true
           return rs.next();
    }
    
    /**
     * @return the conn
     */
    public Connection getConn() {
        return conn;
    }

    /**
     * @param conn the conn to set
     */
    public void setConn(Connection conn) {
        this.conn = conn;
    }

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
     * @return the forename
     */
    public String getForename() {
        return forename;
    }

    /**
     * @param forename the forename to set
     */
    public void setForename(String forename) {
        this.forename = forename;
    }

    /**
     * @return the surname
     */
    public String getSurname() {
        return surname;
    }

    /**
     * @param surname the surname to set
     */
    public void setSurname(String surname) {
        this.surname = surname;
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
     * @return the customerModel
     */
    public static CustomerModel getCustomerModel() {
        return customerModel;
    }

    /**
     * @param aCustomerModel the customerModel to set
     */
    public static void setCustomerModel(CustomerModel aCustomerModel) {
        customerModel = aCustomerModel;
    }
}