/**
 * JsonUtil.java
 * com.ichaoying.util
 * Copyright (c) 2010-2012 ichaoying.com
 * All rights reserved.
 */
package com.zs.util;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import org.codehaus.jackson.map.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * json包装类，转换json和object
 * 
 * @author pany May 28, 2012
 * 
 */
public abstract class JsonUtil {
    // log
    private static final Logger log = LoggerFactory.getLogger(JsonUtil.class);

    // from jackson, 对象包装1器
    private static ObjectMapper objectMapper = new ObjectMapper();

    /**
     * 对象转换为json
     * 
     * @param obj
     * @return
     * 
     */
    public static String toJsonString(Object obj) {
	try {
	    return objectMapper.writeValueAsString(obj);
	} catch (Exception e) {
	    log.error(e.getMessage(), e);
	}
	return null;
    }

    /**
     * 转换json to 对象
     * 
     * @param json
     * @param clazz
     * @return
     */
    public static <T> T toObject(String json, Class<T> clazz) {
	try {
	    return objectMapper.readValue(json, clazz);
	} catch (Exception e) {
	    log.error(e.getMessage(), e);
	}
	return null;
    }

    /**
     * convert json to map object
     * 
     * @param json
     * @return
     */
    @SuppressWarnings("unchecked")
    public static <K, T> Map<K, T> toMap(String json) {
	try {
	    return objectMapper.readValue(json, Map.class);
	} catch (Exception e) {
	    log.error(e.getMessage(), e);
	}
	return null;
    }

    @SuppressWarnings("unchecked")
    public static <K, T> Map<K, T> toMap(String json, Class<K> kclazz,
	    Class<T> tclass) {
	try {
	    return objectMapper.readValue(json, Map.class);
	} catch (Exception e) {
	    log.error(e.getMessage(), e);
	}
	return null;
    }

    /**
     * convert json to list object
     * 
     * @param json
     * @return
     */
    public static List<?> toList(String json) {
	try {
	    return objectMapper.readValue(json, List.class);
	} catch (Exception e) {
	    log.error(e.getMessage(), e);
	}
	return null;
    }

    /**
     * convert json to array object
     * 
     * @param json
     * @return
     */
    @SuppressWarnings("unchecked")
    public static <T> T[] toArray(String json) {
	try {
	    return (T[]) objectMapper.readValue(json, Object[].class);
	} catch (Exception e) {
	    log.error(e.getMessage(), e);
	}
	return null;
    }

    /**
     * 将json转换List装配 clazz类型
     * 
     * @param json
     * @param claz
     *            ch T.Class
     * @return 2012-7-19 上午3:05:28
     * @author pany
     */
    public static <T> List<T> toClassList(String json, Class<T> clazz) {
	try {

	    List<?> list = objectMapper.readValue(json, List.class);
	    List<T> retList = new ArrayList<T>();
	    for (Object o : list) {
		retList.add(objectMapper.convertValue(o, clazz));
	    }
	    return retList;
	} catch (Exception e) {
	    log.error(e.getMessage(), e);
	}
	return null;
    }

    /**
     * json转换为Object[T]类型数组
     * 
     * @param json
     * @param clazz
     * @return 2012-7-19 上午3:43:02
     * @author pany
     */
    public static <T> Object[] toClassArray(String json, Class<T> clazz) {
	try {
	    Object[] objArray = toArray(json);
	    List<T> retList = new ArrayList<T>();
	    if (objArray != null) {
		for (Object obj : objArray) {
		    retList.add((T) objectMapper.convertValue(obj, clazz));
		}
		return retList.toArray();
	    }
	} catch (Exception e) {
	    log.error(e.getMessage(), e);
	}
	return null;
    }

    /**
     * 
     * @param json
     * @param clazz
     *            map value类型class
     * @param kclazz
     *            map key的类型class
     * @return 2012-7-19 上午8:33:39
     * @author pany
     */
    public static <K, T> LinkedHashMap<?, T> toClassLinkMap(String json,
	    Class<T> clazz, Class<K> kclazz) {
	Map<K, T> map = toMap(json);
	LinkedHashMap<Object, T> linkMap = new LinkedHashMap<Object, T>();
	initMap(map, linkMap, clazz, kclazz);
	return linkMap;
    }

    /**
     * 获取TreeMap<Object,T> 类型对象
     * 
     * @param json
     * @param clazz
     *            map value类型class
     * @param kclazz
     *            map key的类型class
     * @return 2012-7-19 上午5:30:37
     * @author pany
     */
    public static <K, T> TreeMap<?, T> toClassTreeMap(String json,
	    Class<T> clazz, Class<K> kclazz) {
	Map<?, ?> map = toMap(json);
	TreeMap<Object, T> treeMap = new TreeMap<Object, T>();
	initMap(map, treeMap, clazz, kclazz);
	return treeMap;
    }

    /**
     * 获取HashMap<Object,T> 类型对象
     * 
     * @param json
     * @param clazz
     *            map value类型class
     * @param kclazz
     *            map key的类型class
     * @return 2012-7-19 上午5:30:37
     * @author pany
     */
    public static <K, T> HashMap<?, T> toClassHashMap(String json,
	    Class<T> clazz, Class<K> kclazz) {
	Map<?, ?> map = toMap(json);
	HashMap<Object, T> hashMap = new HashMap<Object, T>();
	initMap(map, hashMap, clazz, kclazz);
	return hashMap;
    }

    /**
     * 初始化目标map
     * 
     * @param map
     * @param targetMap
     * @param clazz
     *            map value类型class
     * @param kclazz
     *            map key的类型class 2012-7-19 上午8:38:18
     * @author pany
     */
    @SuppressWarnings("rawtypes")
    private static <K, T> void initMap(Map<?, ?> map, Map<Object, T> targetMap,
	    Class<T> clazz, Class<K> kclazz) {
	Iterator it = map.keySet().iterator();
	while (it.hasNext()) {
	    Object key = it.next();
	    Object obj = map.get(key);
	    targetMap.put(getMapKey(kclazz, key),
		    objectMapper.convertValue(obj, clazz));

	}
    }

    /**
     * 返回 Map<Object,List<T>>类型的linkMap;
     * 
     * @param json
     * @param clazz
     *            map value类型class
     * @param kclazz
     *            map key的类型class
     * @return 2012-7-19 上午6:56:02
     * @author pany
     * @param <K>
     */
    public static <K, T> Map<?, List<T>> toClassListLinkMap(String json,
	    Class<T> clazz, Class<K> kclazz) {
	Map<?, ?> map = toMap(json);
	Map<Object, List<T>> linkMap = new LinkedHashMap<Object, List<T>>();
	initClassListMap(map, linkMap, clazz, kclazz);
	return linkMap;
    }

    /**
     * 初始化装配的map
     * 
     * @param map
     * @param newMap
     * @param clazz
     *            map value类型class
     * @param kclazz
     *            map key的类型class 2012-7-19 上午6:56:36
     * @author pany
     */

    @SuppressWarnings("rawtypes")
    private static <K, T> void initClassListMap(Map<?, ?> map,
	    Map<Object, List<T>> newMap, Class<T> clazz, Class<K> kclzz) {
	Iterator it = map.keySet().iterator();
	while (it.hasNext()) {
	    Object key = it.next();
	    Object obj = map.get(key);
	    List list = objectMapper.convertValue(obj, List.class);
	    List<T> newList = new ArrayList<T>();
	    for (Object o : list) {
		newList.add(objectMapper.convertValue(o, clazz));
	    }
	    newMap.put(getMapKey(kclzz, key), newList);
	}
    }

    /**
     * 转换map中的key类型
     * 
     * @param kclazz
     *            map key的类型class
     * @param key
     * @return 2012-7-19 上午8:39:36
     * @author pany
     */
    private static <K> Object getMapKey(Class<K> kclazz, Object key) {
	String className = JavaClassUtil.getShortClassName(kclazz.getName());
	if (className.equals("Integer")) {
	    return Integer.parseInt(key.toString());
	}
	return key;
    }
}
