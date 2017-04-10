/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package utils;

import org.apache.commons.validator.routines.EmailValidator;


/**
 *
 * @author Nota
 */
public class Validator {
    public Validator(){
    }
    
    /**
     * validates an email
     * @param email the email to be validated
     * @return true if the email has a correct structure
     */
    public static boolean validateEmail(String email){
       if (email == null || "".equals(email))
		return false;
	
	email = email.trim();
	
	EmailValidator ev = EmailValidator.getInstance();
	return ev.isValid(email);
    }
}
