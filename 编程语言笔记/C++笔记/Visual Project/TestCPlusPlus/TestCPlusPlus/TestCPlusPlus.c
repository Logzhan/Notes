// TestCPlusPlus.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#pragma warning(disable:4996)

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
    uint8_t ssid[32];      /**< SSID of target AP. */
    uint8_t password[64];  /**< Password of target AP. */
} wifi_sta_config_t;

/** @brief Configuration data for ESP32 AP or STA.
 *
 * The usage of this union (for ap or sta configuration) is determined by the accompanying
 * interface argument passed to esp_wifi_set_config() or esp_wifi_get_config()
 *
 */
typedef union {
    wifi_sta_config_t sta; /**< configuration of STA */
} wifi_config_t;


#define CFG_WIFI_SSID       "log_zhan"             // 配置默认连接的WIFI的SSID
#define CFG_WIFI_PASS       "19931203"            // 配置默认连接的WIFI的密码

wifi_config_t wifi_config = {
    .sta = {
        .ssid = CFG_WIFI_SSID,
        .password = CFG_WIFI_PASS,
    },
};


void Test1() {
    char  OldSSID[32] = { 'O','r','i','g','i','n','P','a'};
    char* NewSSID     = "MySSID";
    /*Copy the string content. */
    memcpy(OldSSID, NewSSID, strlen(NewSSID) + 1);
    /* Output the result. */
    printf("wifi ssid = %s\n", OldSSID);
}

void Test2() {
    //const char* str1 = "this is str1";
    //const char* str2 = "this is str2";
    //char* str = str1;
    //printf("%s\n", str);
    //str = str2;
    //printf("%s\n", str);
}

int main()
{
    Test1();
    //Test2();
    system("pause");
}
