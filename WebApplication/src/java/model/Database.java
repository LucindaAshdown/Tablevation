/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author Nota
 */
public class Database {
    
    /**
     * @return a new connection from the database
     * @throws SQLException 
     * @throws java.lang.ClassNotFoundException 
     */
    public static Connection getConnection() throws SQLException, ClassNotFoundException{
        Class.forName("");
        return DriverManager.getConnection("jdbc:","tablevation","%_tablevation_%");
    }
}
