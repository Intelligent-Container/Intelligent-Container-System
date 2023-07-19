/*
 * uart.c
 *
 * created: 2021/4/30
 *  author:
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "uart.h"
#include "ls1b.h"
#include "ls1b_gpio.h"
#include "ns16550.h"
#include "stdio.h"
#include "led.h"
#include "string.h"
#include "uart.h"
#include "temp.h"
/*******************************************************************
 **��������UART5_set_IO
 **�������ܣ���ʼ��uart��IO��
 **�βΣ���
 **����ֵ����
 **˵����   UART5_RX:60 -- ���ݽ���
            UART5_TX:61 -- ���ݷ���
 *******************************************************************/
void UART5_Config_Init(void)
{
    unsigned int BaudRate = 115200;
    ls1x_uart_init(devUART5, (void *)BaudRate); // ��ʼ������
    ls1x_uart_open(devUART5, NULL);             // �򿪴���
}

void UART4_Config_Init(void)
{
    unsigned int BaudRate = 115200;
    ls1x_uart_init(devUART4, (void *)BaudRate); // ��ʼ������
    ls1x_uart_open(devUART4, NULL);             // �򿪴���
}

char *UART5_Read()
{
    count = ls1x_uart_read(devUART5, buff, 1, NULL);
    if (count > 0)
    {
        printf("�����յ���Ϣ");
        // delay_ms(10);
    }
    else
    {
        return 0;
    }
    count = 0;
}

// int i = 1;
// int flag = 0;
// char temp[1024];
void UART5_Write(char *buff)
{
    if (count > 0)
    {
        // strcpy(buff,strlen(buff));
        // printf("%d:",i);
        ls1x_uart_write(devUART5, buff, strlen(buff), NULL);
        // strcpy(temp[i],buff);
    }
    // if(count = 0 && flag == 1);
    // {
    //     printf("�������");
    //     flag = 0;
    // }
}

char *UART4_Read(void)
{
    count = ls1x_uart_read(devUART4, buff, 1, NULL);
    strcpy(read2, buff);
    return read;
}

void UART4_Write(char *buff)
{
    if (count > 0)
    {
        // strcpy(buff,strlen(buff));
        ls1x_uart_write(devUART4, buff, strlen(buff), NULL);
    }
}

// ����
int UART5_Test(void)
{
    // ��������
    // count = ls1x_uart_read(devUART5, buff, 1, NULL);
    // if (count > 0)
    // {
    //     // ��������
    //     ls1x_uart_write(devUART5, buff, strlen(buff), NULL);
    // }
    count = ls1x_uart_read(devUART5, buff, 256, NULL);
    // delay_ms(500);

    if (strncmp(buff, "0102", 4) == 0)
    {
        char tmp[8] = "0";
        char dev[8] = "0";
        char add[8] = "0";
        char exe[8] = "0";
        char op[8] = "0";
        strncpy(tmp, buff, 8);
        strncpy(dev, &tmp[0], 2);
        strncpy(add, &tmp[2], 2);
        strncpy(exe, &tmp[4], 2);
        strncpy(op, &tmp[6], 2);

        if (strncmp(dev, "01", 2) == 0)
        {
            printf("��������2K1000,");
            if (strncmp(add, "02", 2) == 0)
            {
                printf("���豸��ַ:%s\r\n", add);
                if (strncmp(exe, "00", 2) == 0)
                {
                    // ʮ�����Ʋ���ָ��תΪʮ����
                    int number = 0, i = 0;
                    for (i = 0; op[i] != '\0'; i++)
                    {
                        if (op[i] >= '0' && op[i] <= '9')
                            number = number * 16 + op[i] - '0'; // �ַ�����ASCII��������ֵ��48�����������ַ���ֵ��ȥ�����ַ�'0'��ֵ�õ��������ַ�����ֵ
                        else if (op[i] >= 'A' && op[i] <= 'F')
                            number = number * 16 + op[i] - 'A' + 10;
                        else if (op[i] >= 'a' && op[i] <= 'f')
                            number = number * 16 + op[i] - 'a' + 10;
                    }
                    // printf("%d",number);
                    Fan_Speed_Control(number);
                    printf("����ת��:%d",number);
                }
                else if (strncmp(exe, "01", 2) == 0)
                {
                    if (strncmp(op, "00", 2) == 0)
                    {
                        Cement_Heat(CEMENT_OFF);
                        printf("���ȹ�");
                    }

                    else if (strncmp(op, "01", 2) == 0)
                    {
                        Cement_Heat(CEMENT_ON);
                        printf("���ȿ�");
                    }
                }
            }

            // char i = "00";
            // strncpy(i,&tmp[4],2);
            // switch (i)
            // {
            // case 01:
            //     printf("���Ʒ���\r\n");
            //     break;

            // default:
            //     break;
            // }
        }
    }
    else if (strncmp(buff, "time", 4) == 0)
    {
        char tmp[8] = "0";
        char time[8] = "0";
        strncpy(tmp,buff,7);
        strncpy(time,&buff[4],3);
        int number = 0, i = 0;
                    for (i = 0; time[i] != '\0'; i++)
                    {
                        if (time[i] >= '0' && time[i] <= '9')
                            number = number * 16 + time[i] - '0'; // �ַ�����ASCII��������ֵ��48�����������ַ���ֵ��ȥ�����ַ�'0'��ֵ�õ��������ַ�����ֵ
                        else if (time[i] >= 'A' && time[i] <= 'F')
                            number = number * 16 + time[i] - 'A' + 10;
                        else if (time[i] >= 'a' && time[i] <= 'f')
                            number = number * 16 + time[i] - 'a' + 10;
                    }
        printf("��ʱ:%dms",number);
        return number;
    }

    /////////////////
    // if (strncmp(buff, "010101", 6) == 0)
    // {
    //     LED_All_ON();
    //     Fan_Speed_Control(50);
    // }
    // if (strncmp(buff, "010100", 6) == 0)
    // {
    //     LED_All_OFF();
    //     Fan_Speed_Control(0);
    //     // char *t = &buff[4];
    //     char str[100];
    //     strncpy(str,&buff[4],2);
    //     printf("%s\r\n",str);
    // }
    // if (strncmp(buff, "010102", 6) == 0)
    // {
    //     LED_Waterfall();
    // }
    /////////////

    // if(strncmp(buff,"led_on",6) == 0) //�Ƚ�ǰn���ֽ�
    // {
    //     LED_All_ON();// ����LED
    // }
    // if(strncmp(buff,"led_off",6) == 0)
    // {
    //     LED_All_OFF();//�ر�LED
    // }
    // if(strncmp(buff,"led_demo",6)==0)
    // {
    //     LED_Waterfall();//��ˮ��
    //     LED_Waterfall();
    // }
}

// ����
void UART4_Test(void)
{
    // ��������
    // count = ls1x_uart_read(devUART5, buff, 1, NULL);
    // if (count > 0)
    // {
    //     // ��������
    //     ls1x_uart_write(devUART5, buff, strlen(buff), NULL);
    // }
    count = ls1x_uart_read(devUART4, buff, 256, NULL);
    // delay_ms(500);

    if (strncmp(buff, "0102", 4) == 0)
    {
        char tmp[8] = "0";
        char dev[8] = "0";
        char add[8] = "0";
        char exe[8] = "0";
        char op[8] = "0";
        strncpy(tmp, buff, 8);
        strncpy(dev, &tmp[0], 2);
        strncpy(add, &tmp[2], 2);
        strncpy(exe, &tmp[4], 2);
        strncpy(op, &tmp[6], 2);

        if (strncmp(dev, "01", 2) == 0)
        {
            printf("��������2K1000,");
            if (strncmp(add, "02", 2) == 0)
            {
                printf("���豸��ַ:%s\r\n", add);
                if (strncmp(exe, "00", 2) == 0)
                {
                    // ʮ�����Ʋ���ָ��תΪʮ����
                    int number = 0, i = 0;
                    for (i = 0; op[i] != '\0'; i++)
                    {
                        if (op[i] >= '0' && op[i] <= '9')
                            number = number * 16 + op[i] - '0'; // �ַ�����ASCII��������ֵ��48�����������ַ���ֵ��ȥ�����ַ�'0'��ֵ�õ��������ַ�����ֵ
                        else if (op[i] >= 'A' && op[i] <= 'F')
                            number = number * 16 + op[i] - 'A' + 10;
                        else if (op[i] >= 'a' && op[i] <= 'f')
                            number = number * 16 + op[i] - 'a' + 10;
                    }
                    // printf("%d",number);
                    Fan_Speed_Control(number);
                    printf("����ת��:%d",number);
                }
                else if (strncmp(exe, "01", 2) == 0)
                {
                    if (strncmp(op, "00", 2) == 0)
                    {
                        Cement_Heat(CEMENT_OFF);
                        printf("���ȹ�");
                    }

                    else if (strncmp(op, "01", 2) == 0)
                    {
                        Cement_Heat(CEMENT_ON);
                        printf("���ȿ�");
                    }
                }
            }
        }
    }
    else if (strncmp(buff, "time", 4) == 0)
    {
        char tmp[8] = "0";
        char time[8] = "0";
        strncpy(tmp,buff,7);
        strncpy(time,&buff[4],3);
        int number = 0, i = 0;
                    for (i = 0; time[i] != '\0'; i++)
                    {
                        if (time[i] >= '0' && time[i] <= '9')
                            number = number * 16 + time[i] - '0'; // �ַ�����ASCII��������ֵ��48�����������ַ���ֵ��ȥ�����ַ�'0'��ֵ�õ��������ַ�����ֵ
                        else if (time[i] >= 'A' && time[i] <= 'F')
                            number = number * 16 + time[i] - 'A' + 10;
                        else if (time[i] >= 'a' && time[i] <= 'f')
                            number = number * 16 + time[i] - 'a' + 10;
                    }
        printf("��ʱ:%dms",number);
        return number;
    }
}

// char *UART4_Test(void)
// {
//     // ��������
//     // count = ls1x_uart_read(devUART4, buff, 1, NULL);
//     // if (count > 0)
//     // {
//     //     // ��������
//     //     ls1x_uart_write(devUART4, buff, strlen(buff), NULL);
//     // }

//     ls1x_uart_read(devUART4, buff, 256, NULL);
//     delay_ms(500);

//     if (strncmp(buff, "010101", 6) == 0)
//     {
//         LED_All_ON();
//     }
//     if (strncmp(buff, "010100", 6) == 0)
//     {
//         LED_All_OFF();
//     }
//     if (strncmp(buff, "010102", 6) == 0)
//     {
//         LED_Waterfall();
//     }
// }
