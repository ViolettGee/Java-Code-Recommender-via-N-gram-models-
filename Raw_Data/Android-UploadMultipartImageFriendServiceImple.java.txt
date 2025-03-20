package com.zs.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.zs.dao.IBaseDao;
import com.zs.po.Friend;
import com.zs.service.IFriendService;


@Service("FriendServiceImple")
public class FriendServiceImple implements  IFriendService{

	
	@Autowired
	private IBaseDao baseDao;
	
	
	public Friend findFriendShip(Integer userid, Integer friendId) {
		String hql ="from Friend where userid = ? and friendId = ?";
		Object[] params = new Object[2];
		params[0] = userid;
		params[1] = friendId;
		List<Friend> findByHql = baseDao.findByHql(hql, params);
		if(findByHql!=null &&findByHql.size()>0){
			return findByHql.get(0);
		}
		return null;
	}

}
