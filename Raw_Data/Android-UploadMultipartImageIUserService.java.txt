package com.zs.service;

import org.springframework.transaction.annotation.Transactional;

import com.zs.po.User;
@Transactional
public interface IUserService {
	
	User findUserForID(String mail) throws Exception ;

	boolean saveUser(User user) throws Exception;
	
	User findUserForUserNameOrEmail(String username) throws Exception ;
}
