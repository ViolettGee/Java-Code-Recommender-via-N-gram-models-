package com.zs.action;

import java.awt.Graphics;


import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

import javax.imageio.ImageIO;
import javax.servlet.http.HttpServletResponse;

import freemarker.log.Logger;
import io.rong.models.FormatType;
import io.rong.models.SdkHttpResult;
import io.rong.utils.ApiHttpClient;

import org.apache.struts2.ServletActionContext;
import org.apache.struts2.convention.annotation.Action;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;

import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionSupport;


@Controller
public class UploadFile extends  ActionSupport {
	
/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	private File[] file;//文件数组
	private String description;//说说内容
	public File[] getFile() {
		return file;
	}
	public void setFile(File[] file) {
		this.file = file;
	}
	
	
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}
	@Action("/upload")
	public void upload()  {
		System.out.println("上传的文件="+Arrays.toString(file));
		System.out.println("说说内容="+description);
	}
	
	
	
}
