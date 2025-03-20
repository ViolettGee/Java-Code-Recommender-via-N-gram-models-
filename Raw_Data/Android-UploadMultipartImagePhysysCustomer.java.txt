package com.zs.po;

public class PhysysCustomer {

	private String name;
	private String degree;
	private String cardNo;
	private String balance;
	private String idNo;
	private String birthday;
	private String createDate;
	private String sex;
	private String address;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getDegree() {
		return degree;
	}
	public void setDegree(String degree) {
		this.degree = degree;
	}
	public String getCardNo() {
		return cardNo;
	}
	public void setCardNo(String cardNo) {
		this.cardNo = cardNo;
	}
	public String getBalance() {
		return balance;
	}
	public void setBalance(String balance) {
		this.balance = balance;
	}
	public String getIdNo() {
		return idNo;
	}
	public void setIdNo(String idNo) {
		this.idNo = idNo;
	}
	public String getBirthday() {
		return birthday;
	}
	public void setBirthday(String birthday) {
		this.birthday = birthday;
	}
	public String getCreateDate() {
		return createDate;
	}
	public void setCreateDate(String createDate) {
		this.createDate = createDate;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	@Override
	public String toString() {
		return "PhysysCustomer [address=" + address + ", balance=" + balance
				+ ", birthday=" + birthday + ", cardNo=" + cardNo
				+ ", createDate=" + createDate + ", degree=" + degree
				+ ", idNo=" + idNo + ", name=" + name + ", sex=" + sex + "]";
	}

	
}
