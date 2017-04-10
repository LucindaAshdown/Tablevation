/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.SQLException;

/**
 * An interface representing a generic model
 * @author Nota
 */
public interface Model {
    /**
     * creates the instance of the class implementing the interface
     * @throws java.sql.SQLException
     */
    public void insert() throws SQLException;
    
    /**
     * updates the instance of the class implementing the interface
     */
    public void update();
}
