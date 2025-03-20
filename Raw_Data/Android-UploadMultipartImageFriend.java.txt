package com.zs.po;

import java.sql.Timestamp;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import static javax.persistence.GenerationType.IDENTITY;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.UniqueConstraint;

/**
 * Friend entity. @author MyEclipse Persistence Tools
 */
@Entity
@Table(name = "friend", catalog = "graduate_system", uniqueConstraints = @UniqueConstraint(columnNames = {
		"user_id", "friend_id" }))
public class Friend implements java.io.Serializable {

	// Fields

	private Integer id;
	private Integer userId;
	private Integer friendId;
	private Integer status;
	private Timestamp timestamp;

	// Constructors

	/** default constructor */
	public Friend() {
	}

	/** full constructor */
	public Friend(Integer userId, Integer friendId, Integer status,
			Timestamp timestamp) {
		this.userId = userId;
		this.friendId = friendId;
		this.status = status;
		this.timestamp = timestamp;
	}

	// Property accessors
	@Id
	@GeneratedValue(strategy = IDENTITY)
	@Column(name = "id", unique = true, nullable = false)
	public Integer getId() {
		return this.id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	@Column(name = "user_id", nullable = false)
	public Integer getUserId() {
		return this.userId;
	}

	public void setUserId(Integer userId) {
		this.userId = userId;
	}

	@Column(name = "friend_id", nullable = false)
	public Integer getFriendId() {
		return this.friendId;
	}

	public void setFriendId(Integer friendId) {
		this.friendId = friendId;
	}

	@Column(name = "status", nullable = false)
	public Integer getStatus() {
		return this.status;
	}

	public void setStatus(Integer status) {
		this.status = status;
	}

	@Column(name = "timestamp", nullable = false, length = 19)
	public Timestamp getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Timestamp timestamp) {
		this.timestamp = timestamp;
	}

}