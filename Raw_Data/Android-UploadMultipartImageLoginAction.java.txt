/*
 * $Id: Login.java 471756 2006-11-06 15:01:43Z husted $
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package com.zs.action;

import org.apache.struts2.convention.annotation.Action;
import org.apache.struts2.convention.annotation.Result;
import org.apache.struts2.convention.annotation.Results;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionSupport;
import com.zs.po.Login;
import com.zs.service.ILoginService;
@Controller
@Results({  
	  @Result(name="input", location="login/Login.jsp"),
	  @Result(name="succ", location="login/Welcome.jsp")
	}) 
public class LoginAction extends ActionSupport {

    /**
	 * 
	 */
	private static final long serialVersionUID = 5033459742031477727L;
	
	@Autowired
	private ILoginService loginService;
	private String username;
	private String password;
	
	@Action("/Login")
	public String login() throws Exception {
		
		Login lg = loginService.getByID(username);
		if(lg == null)
			return "input";
		else
		{
			 ActionContext.getContext().getSession().put("user", lg);
	         return "succ";
		}
    }
	
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    } 

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

}