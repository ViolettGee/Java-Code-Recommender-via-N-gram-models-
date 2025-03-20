package com.zs.service;

import com.zs.po.Login;

public interface ILoginService {
	
	public Login getByID(String username);
	
	public boolean login(String username,String password);
}
