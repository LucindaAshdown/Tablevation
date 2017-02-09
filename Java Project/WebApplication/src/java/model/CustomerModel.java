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
    /**
     * constructor that connect the class to the database
     * @throws ClassNotFoundException 
     * @throws java.sql.SQLException 
     */
    public CustomerModel() throws ClassNotFoundException, SQLException{
       conn = Database.getConnection();
    }
    
    @Override
    public void insert() {
        PreparedStatement ps;
        String query = "INSERT INTO Customer VALUES (?,?,?,?,?)";
    }

    @Override
    public void update() {
        PreparedStatement ps;
        String query = "UPDATE Customer SET (?,?,?)";
    }

    @Override
    public LinkedList<Object> select(LinkedList<Object> keys) {
        return null;
    }
}
