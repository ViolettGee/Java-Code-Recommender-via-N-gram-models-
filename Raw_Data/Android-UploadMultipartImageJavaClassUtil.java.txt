/**
 * JavaClassUtil.java
 * com.ichaoying.util
 * Copyright (c) 2010-2012 ichaoying.com
 * All rights reserved.
 */
package com.zs.util;

import java.io.File;
import java.net.URL;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

import org.springframework.util.AntPathMatcher;

/**
 * 静态类，获取java类信息的方法工具
 * 
 * @author pany
 * @version 1.1,2012-08-20 add ant matcher support
 * 
 */
public abstract class JavaClassUtil {
    private static AntPathMatcher pathMatcher = new AntPathMatcher();

    /**
     * Determine the root directory for the given location.
     * <p>
     * Used for determining the starting point for file matching, resolving the
     * root directory location to a <code>java.io.File</code> and passing it
     * into <code>retrieveMatchingFiles</code>, with the remainder of the
     * location as pattern.
     * <p>
     * Will return "/WEB-INF" for the pattern "/WEB-INF/*.xml", for example.
     * 
     * @param location
     *            the location to check
     * @return the part of the location that denotes the root directory
     * @see #retrieveMatchingFiles
     */
    private static String determineRootDir(String location) {
	int prefixEnd = location.indexOf(":") + 1;
	int rootDirEnd = location.length();
	while (rootDirEnd > prefixEnd
		&& pathMatcher.isPattern(location.substring(prefixEnd,
			rootDirEnd))) {
	    rootDirEnd = location.lastIndexOf('/', rootDirEnd - 1) ;
	}
	if (rootDirEnd == 0) {
	    rootDirEnd = prefixEnd;
	}
	return location.substring(0, rootDirEnd);
    }

    /**
     * 根据模糊包名称匹配包下的所有的类
     * 
     * @param packageNameMatcher
     * @return
     */
    public static List<Class<?>> getClassNameByPackageNameMatcher(
	    String packageNameMatcher) {
	String path = packageNameMatcher.replace('.', '/');
	Set<String> classes;
	if(pathMatcher.isPattern(path)){
        	String rootDirPath = determineRootDir(path);
        	classes = getClassFullNameByPackageName(rootDirPath.replace('/', '.'));
	}else{
	    classes = getClassFullNameByPackageName(packageNameMatcher);
	}
	try {
	    ArrayList<Class<?>> classList = new ArrayList<Class<?>>();
	    // 按照ant格式匹配
	    String classMatcher = path + "/*";
	    for (String clazz : classes) {
		if(pathMatcher.match(classMatcher,clazz.replace('.', '/'))){
		    classList.add(Class.forName(clazz));
		}
	    }
	    return classList;
	} catch (ClassNotFoundException e) {
	    // TODO Auto-generated catch block
	    throw new RuntimeException(e.getMessage());
	}
    }

    /**
     * 指定包名称获取所有的类
     * 
     * @param packageName
     * @return
     */
    public static List<Class<?>> getClassNameByPackageName(String packageName) {
	Set<String> classes = getClassFullNameByPackageName(packageName);

	try {
	    ArrayList<Class<?>> classList = new ArrayList<Class<?>>();
	    for (String clazz : classes) {
		classList.add(Class.forName(clazz));
	    }
	    return classList;
	} catch (ClassNotFoundException e) {
	    // TODO Auto-generated catch block
	    throw new RuntimeException(e.getMessage());
	}
    }

    private static Set<String> getClassFullNameByPackageName(String packageName) {
	try {
	    ClassLoader classLoader = Thread.currentThread()
		    .getContextClassLoader();
	    assert classLoader != null;
	    String path = packageName.replace('.', '/');
	    Enumeration<URL> resources = classLoader.getResources(path);
	    List<String> dirs = new ArrayList<String>();
	    while (resources.hasMoreElements()) {
		URL resource = resources.nextElement();
		dirs.add(resource.getFile());
	    }
	    TreeSet<String> classes = new TreeSet<String>();
	    for (String directory : dirs) {
		classes.addAll(findClasses(directory, packageName));
	    }
	    return classes;
	} catch (Exception e) {
	    throw new RuntimeException(e.getMessage());
	}
    }

    /**
     * Recursive method used to find all classes in a given directory and
     * subdirs. Adapted from http://snippets.dzone.com/posts/show/4831 and
     * extended to support use of JAR files
     * 
     * @param directory
     *            The base directory
     * @param packageName
     *            The package name for classes found inside the base directory
     * @return The classes
     * @throws ClassNotFoundException
     */
    private static TreeSet<String> findClasses(String directory,
	    String packageName) throws Exception {
	TreeSet<String> classes = new TreeSet<String>();
	if (directory.startsWith("file:") && directory.contains("!")) {
	    String[] split = directory.split("!");
	    URL jar = new URL(split[0]);
	    ZipInputStream zip = new ZipInputStream(jar.openStream());
	    ZipEntry entry = null;
	    while ((entry = zip.getNextEntry()) != null) {
		if (entry.getName().endsWith(".class")) {
		    String className = entry.getName().replaceAll("[$].*", "")
			    .replaceAll("[.]class", "").replace('/', '.');
		    classes.add(className);
		}
	    }
	}
	File dir = new File(directory);
	if (!dir.exists()) {
	    return classes;
	}
	File[] files = dir.listFiles();
	for (File file : files) {
	    if (file.isDirectory()) {
		assert !file.getName().contains(".");
		classes.addAll(findClasses(file.getAbsolutePath(), packageName
			+ "." + file.getName()));
	    } else if (file.getName().endsWith(".class")) {
		classes.add(packageName
			+ '.'
			+ file.getName().substring(0,
				file.getName().length() - 6));
	    }
	}
	return classes;
    }

    /**
     * 转化get属性方法名为属性名
     * 
     * @param methodName
     * @return
     */
    public static String methodGetNameToProperName(String methodName) {
	return methodNameToProperName(methodName, "get");
    }

    public static String methodNameToProperName(String methodName, String prifix) {
	if ((methodName.startsWith(prifix)) && methodName.length() > 3) {
	    String ret = methodName.substring(3, 4).toLowerCase();
	    if (methodName.length() > 4)
		ret += methodName.substring(4);

	    return ret;
	} else {
	    return methodName;
	}
    }

    /**
     * 得到类的短名称
     * 
     * @param className
     * @return
     */
    public static String getShortClassName(String className) {
	int pos = className.lastIndexOf(".");
	if (pos == -1) {
	    return className;
	}
	return className.substring(pos + 1);
    }

}
