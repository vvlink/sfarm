VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "开源智慧农场（sfarm）项目数据订阅"
   ClientHeight    =   6675
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   11205
   LinkTopic       =   "Form1"
   ScaleHeight     =   6675
   ScaleWidth      =   11205
   StartUpPosition =   3  '窗口缺省
   Begin VB.PictureBox Picture1 
      Height          =   3000
      Left            =   4800
      ScaleHeight     =   2940
      ScaleWidth      =   5940
      TabIndex        =   14
      Top             =   2880
      Width           =   6000
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Interval        =   1000
      Left            =   9120
      Top             =   120
   End
   Begin VB.CommandButton Command2 
      Caption         =   "开启订阅"
      Height          =   615
      Left            =   720
      TabIndex        =   12
      Top             =   5160
      Width           =   1095
   End
   Begin VB.Frame Frame2 
      Caption         =   "接收消息"
      Height          =   3015
      Left            =   3000
      TabIndex        =   11
      Top             =   2880
      Width           =   1575
      Begin VB.ListBox List2 
         Height          =   2400
         Left            =   240
         TabIndex        =   13
         Top             =   360
         Width           =   1095
      End
   End
   Begin VB.Frame Frame5 
      Caption         =   "设备名（土壤）"
      Height          =   855
      Left            =   360
      TabIndex        =   9
      Top             =   3840
      Width           =   2175
      Begin VB.TextBox a1 
         Height          =   495
         Left            =   120
         TabIndex        =   10
         Text            =   "a1"
         Top             =   240
         Width           =   1935
      End
   End
   Begin VB.Frame Frame4 
      Caption         =   "项目名"
      Height          =   855
      Left            =   360
      TabIndex        =   7
      Top             =   2880
      Width           =   2175
      Begin VB.TextBox pname 
         Height          =   495
         Left            =   120
         TabIndex        =   8
         Text            =   "sf189"
         Top             =   240
         Width           =   1935
      End
   End
   Begin VB.Frame Frame1 
      Caption         =   "设置SIoT服务器地址："
      Height          =   2175
      Left            =   360
      TabIndex        =   0
      Top             =   480
      Width           =   10575
      Begin VB.TextBox ipwd 
         Height          =   375
         Left            =   5640
         TabIndex        =   6
         Text            =   "scope"
         Top             =   1200
         Width           =   2655
      End
      Begin VB.TextBox iname 
         Height          =   375
         Left            =   1560
         TabIndex        =   4
         Text            =   "scope"
         Top             =   1200
         Width           =   2655
      End
      Begin VB.TextBox Server 
         Height          =   375
         Left            =   1560
         TabIndex        =   2
         Text            =   "192.168.1.88"
         Top             =   600
         Width           =   2655
      End
      Begin VB.Label Label3 
         Caption         =   "密码："
         Height          =   375
         Left            =   4800
         TabIndex        =   5
         Top             =   1320
         Width           =   855
      End
      Begin VB.Label Label2 
         Caption         =   "用户名："
         Height          =   495
         Left            =   360
         TabIndex        =   3
         Top             =   1320
         Width           =   975
      End
      Begin VB.Label Label1 
         Caption         =   "服务器地址："
         Height          =   375
         Left            =   360
         TabIndex        =   1
         Top             =   720
         Width           =   1935
      End
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim begin As Boolean, oldstr As String, x As Long, y As Long
Sub draw(val)
If x = 0 Then
    x = 100
    y = val * 3
ElseIf x > 6000 Then
    Picture1.Cls
    x = 100
    y = val * 3
Else
    Picture1.Line (x, 3000 - y)-(x + 100, 3000 - val * 3), vbRed
    x = x + 100
    y = val * 3
End If
End Sub


Private Sub Command2_Click()
If Not begin Then
    Timer1.Enabled = Not begin   '注意Timer控件的enable属性在初始化状态下为false
    MsgBox ("开始接收数据！")
    Command2.Caption = "停止订阅"
    begin = Not begin
Else
    Timer1.Enabled = Not begin
    MsgBox ("停止接收数据！")
    Command2.Caption = "开始订阅"
    begin = Not begin
End If
End Sub

Private Sub Timer1_Timer()
    On Error Resume Next
    Dim rNum As String
    rNum = Int((9999) * Rnd(Now()) + 1)
    
    Dim getmsg, strURL2, code
    Dim topicstr As String, val As String
    topicstr = pname.Text & "/" & a1.Text
    Set xmlobject = CreateObject("Microsoft.XMLHTTP")
    strURL = "Http://" & Server.Text & ":8080/lastmessage?topic=" & topicstr & "&iname=" & iname.Text & "&ipwd=" & ipwd.Text & "&num=" & rNum
       
    xmlobject.Open "GET", strURL, False
    xmlobject.send
    If xmlobject.ReadyState = 4 Then
        getmsg = xmlobject.responseText
        'Print getmsg
        code = Json("code", getmsg)
        'Print code
        '用字符串的方式找出
        If getmsg <> oldstr And code = "1" Then
            searchchar1 = "Content"
            searchchar2 = "Created"
            charpos1 = InStr(1, getmsg, searchchar1, 1)
            charpos2 = InStr(1, getmsg, searchchar2, 1)
            val = Mid(getmsg, charpos1 + 10, charpos2 - 3 - charpos1 - 10)
            'Print val
            draw (val)
            List2.AddItem val
            oldstr = getmsg
        End If
    End If
    Set xmlobject = Nothing
End Sub

Public Function Json(ByVal JSONPath As String, ByVal JSONString As String) As Variant
    On Error Resume Next
    Dim JS As Object
    If JSONString = "" Then Exit Function
    Set JS = CreateObject("MSScriptControl.ScriptControl")
    JS.Language = "JScript"
    Json = JS.Eval("JSON=" & JSONString & ";JSON." & JSONPath & ";")
    Set JS = Nothing
End Function


