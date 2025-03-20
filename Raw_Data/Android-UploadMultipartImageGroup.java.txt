package com.zs.po;

import java.sql.Timestamp;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import static javax.persistence.GenerationType.IDENTITY;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * Group entity. @author MyEclipse Persistence Tools
 */
@Entity
@Table(name = "group", catalog = "graduate_system")
public class Group implements java.io.Serializable {

	// Fields

	private Integer id;
	private String name;
	private String portrait;
	private String introduce;
	private Integer number;
	private Integer maxNumber;
	private Integer createUserId;
	private Timestamp creatDatetime;

	// Constructors

	/** default constructor */
	public Group() {
	}

	/** minimal constructor */
	public Group(String name, Integer number, Integer maxNumber,
			Integer createUserId, Timestamp creatDatetime) {
		this.name = name;
		this.number = number;
		this.maxNumber = maxNumber;
		this.createUserId = createUserId;
		this.creatDatetime = creatDatetime;
	}

	/** full constructor */
	public Group(String name, String portrait, String introduce,
			Integer number, Integer maxNumber, Integer createUserId,
			Timestamp creatDatetime) {
		this.name = name;
		this.portrait = portrait;
		this.introduce = introduce;
		this.number = number;
		this.maxNumber = maxNumber;
		this.createUserId = createUserId;
		this.creatDatetime = creatDatetime;
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

	@Column(name = "name", nullable = false, length = 64)
	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Column(name = "portrait", length = 128)
	public String getPortrait() {
		return this.portrait;
	}

	public void setPortrait(String portrait) {
		this.portrait = portrait;
	}

	@Column(name = "introduce", length = 256)
	public String getIntroduce() {
		return this.introduce;
	}

	public void setIntroduce(String introduce) {
		this.introduce = introduce;
	}

	@Column(name = "number", nullable = false)
	public Integer getNumber() {
		return this.number;
	}

	public void setNumber(Integer number) {
		this.number = number;
	}

	@Column(name = "max_number", nullable = false)
	public Integer getMaxNumber() {
		return this.maxNumber;
	}

	public void setMaxNumber(Integer maxNumber) {
		this.maxNumber = maxNumber;
	}

	@Column(name = "create_user_id", nullable = false)
	public Integer getCreateUserId() {
		return this.createUserId;
	}

	public void setCreateUserId(Integer createUserId) {
		this.createUserId = createUserId;
	}

	@Column(name = "creat_datetime", nullable = false, length = 19)
	public Timestamp getCreatDatetime() {
		return this.creatDatetime;
	}

	public void setCreatDatetime(Timestamp creatDatetime) {
		this.creatDatetime = creatDatetime;
	}

}