package com.zs.po;

import java.sql.Timestamp;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import static javax.persistence.GenerationType.IDENTITY;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * GroupUser entity. @author MyEclipse Persistence Tools
 */
@Entity
@Table(name = "group_user", catalog = "graduate_system")
public class GroupUser implements java.io.Serializable {

	// Fields

	private Integer id;
	private Integer groupId;
	private Integer userId;
	private Integer role;
	private Timestamp timestamp;

	// Constructors

	/** default constructor */
	public GroupUser() {
	}

	/** full constructor */
	public GroupUser(Integer groupId, Integer userId, Integer role,
			Timestamp timestamp) {
		this.groupId = groupId;
		this.userId = userId;
		this.role = role;
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

	@Column(name = "group_id", nullable = false)
	public Integer getGroupId() {
		return this.groupId;
	}

	public void setGroupId(Integer groupId) {
		this.groupId = groupId;
	}

	@Column(name = "user_id", nullable = false)
	public Integer getUserId() {
		return this.userId;
	}

	public void setUserId(Integer userId) {
		this.userId = userId;
	}

	@Column(name = "role", nullable = false)
	public Integer getRole() {
		return this.role;
	}

	public void setRole(Integer role) {
		this.role = role;
	}

	@Column(name = "timestamp", nullable = false, length = 19)
	public Timestamp getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Timestamp timestamp) {
		this.timestamp = timestamp;
	}

}