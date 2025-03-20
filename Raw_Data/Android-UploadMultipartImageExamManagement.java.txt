package com.zs.po;

import java.util.List;

public class ExamManagement {

	private List<ExamData> data;
	private String errMsg;
	private String success;
	
	public String getErrMsg() {
		return errMsg;
	}
	public void setErrMsg(String errMsg) {
		this.errMsg = errMsg;
	}
	public String getSuccess() {
		return success;
	}
	public void setSuccess(String success) {
		this.success = success;
	}
	public List<ExamData> getData() {
		return data;
	}
	public void setData(List<ExamData> data) {
		this.data = data;
	}
}
