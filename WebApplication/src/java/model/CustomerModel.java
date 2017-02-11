/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.LinkedList;

/**
 *
 * @author Francesco David Nota
 */
public class CustomerModel implements Model{
    
    private final Connection conn;
    private String email;
    private String password;
    private String forename;
    private String surname;
    private String contactNumber;
    private static CustomerModel customerModel = null;
            
    /**
     * constructor that connect the class to the database
     * @throws ClassNotFoundException 
     * @throws java.sql.SQLException 
     */
    private CustomerModel() throws ClassNotFoundException, SQLException{
       conn = Database.getConnection();
    }
    
    public static CustomerModel getInstance() throws SQLException, ClassNotFoundException{
       if(customerModel == null)
           customerModel = new CustomerModel();
       return customerModel;
    }
    
    @Override
    public void insert() {
        String query = "INSERT INTO Customer VALUES (?,?,?,?,?)";
        try{
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setString(1, this.email);
            ps.setString(2, this.password);
            ps.setString(3, this.forename);
            ps.setString(4, this.surname);
            ps.setString(5, this.contactNumber);
            
            ps.executeUpdate();
        }catch(SQLException ex){
            ex.printStackTrace();
        }
    }

    @Override
    public void update() {
        String query = "UPDATE Customer SET (?,?,?) WHERE Customer.email = ?";
        try{
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setString(1, this.password);
            ps.setString(2, this.forename);
            ps.setString(3, this.surname);
            ps.setString(4, this.email);
            
            ps.executeUpdate();
        }catch(SQLException ex){
            ex.printStackTrace();
        }
    }

    @Override
    public LinkedList<Object> select(LinkedList<Object> keys) {
        return null;
    }
}
