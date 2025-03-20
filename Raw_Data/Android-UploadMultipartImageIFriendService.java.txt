package com.zs.service;

import org.springframework.transaction.annotation.Transactional;

import com.zs.po.Friend;

@Transactional
public interface IFriendService {
	
	Friend findFriendShip (Integer userid, Integer friendId);

}
