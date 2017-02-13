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
}
