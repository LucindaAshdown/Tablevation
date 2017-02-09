/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.util.LinkedList;

/**
 * An interface representing a generic model
 * @author Nota
 */
public interface Model {
    /**
     * @param model the object instance to be inserted in the database of the class that 
     * implements the model interface 
     */
    public void insert();
    
    /**
     * @param model the object instance to be updated in the database of the class that 
     * implements the model interface 
     */
    public void update();
    
    /**
     * @param keys the list of keys to be used in the query to select
     * the objects from the database
     * @return the list of the objects created after the query has been executed
     */
    public LinkedList<Object> select(LinkedList<Object> keys);
}
