VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "��Դ�ǻ�ũ����sfarm����Ŀ�豸����"
   ClientHeight    =   6840
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   11205
   LinkTopic       =   "Form1"
   ScaleHeight     =   6840
   ScaleWidth      =   11205
   StartUpPosition =   3  '����ȱʡ
   Begin VB.Frame Frame6 
      Caption         =   "�豸������ŷ���"
      Height          =   855
      Left            =   360
      TabIndex        =   17
      Top             =   4800
      Width           =   2175
      Begin VB.TextBox d2 
         Height          =   495
         Left            =   120
         TabIndex        =   18
         Text            =   "d2"
         Top             =   240
         Width           =   1935
      End
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Interval        =   1000
      Left            =   9120
      Top             =   120
   End
   Begin VB.CommandButton Command2 
      Caption         =   "��������"
      Height          =   615
      Left            =   360
      TabIndex        =   14
      Top             =   5880
      Width           =   1095
   End
   Begin VB.Frame Frame2 
      Caption         =   "������Ϣ"
      Height          =   3615
      Left            =   6960
      TabIndex        =   13
      Top             =   2880
      Width           =   3975
      Begin VB.ListBox List2 
         Height          =   2940
         Left            =   240
         TabIndex        =   16
         Top             =   360
         Width           =   3375
      End
   End
   Begin VB.Frame Frame5 
      Caption         =   "�豸����������"
      Height          =   855
      Left            =   360
      TabIndex        =   11
      Top             =   3840
      Width           =   2175
      Begin VB.TextBox a1 
         Height          =   495
         Left            =   120
         TabIndex        =   12
         Text            =   "a1"
         Top             =   240
         Width           =   1935
      End
   End
   Begin VB.Frame Frame4 
      Caption         =   "��Ŀ��"
      Height          =   855
      Left            =   360
      TabIndex        =   9
      Top             =   2880
      Width           =   2175
      Begin VB.TextBox pname 
         Height          =   495
         Left            =   120
         TabIndex        =   10
         Text            =   "sf189"
         Top             =   240
         Width           =   1935
      End
   End
   Begin VB.Frame Frame3 
      Caption         =   "���Ϳ���ָ��"
      Height          =   3615
      Left            =   3360
      TabIndex        =   8
      Top             =   2880
      Width           =   3015
      Begin VB.ListBox List1 
         Height          =   3120
         Left            =   120
         TabIndex        =   15
         Top             =   360
         Width           =   2775
      End
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Զ�̽�ˮ"
      Height          =   615
      Left            =   1800
      TabIndex        =   7
      Top             =   5880
      Width           =   1095
   End
   Begin VB.Frame Frame1 
      Caption         =   "����SIoT��������ַ��"
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
         Caption         =   "���룺"
         Height          =   375
         Left            =   4800
         TabIndex        =   5
         Top             =   1320
         Width           =   855
      End
      Begin VB.Label Label2 
         Caption         =   "�û�����"
         Height          =   495
         Left            =   360
         TabIndex        =   3
         Top             =   1320
         Width           =   975
      End
      Begin VB.Label Label1 
         Caption         =   "��������ַ��"
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
Dim begin As Boolean, oldstr As String
Private Sub Command1_Click()
    On Error Resume Next
    Dim topicstr As String, strURL As String
    rNum = Int((9999) * Rnd(Now()) + 1)
    topicstr = pname.Text & "/" & d2.Text
    Set xmlobject = CreateObject("Microsoft.XMLHTTP")
    strURL = "Http://" & Server.Text & ":8080/publish?topic=" & topicstr & "&msg=1&iname=" & iname.Text & "&ipwd=" & ipwd.Text & "&r=" & rNum
    Debug.Print strURL
    xmlobject.Open "GET", strURL, False
    xmlobject.send
    If xmlobject.ReadyState = 4 Then
        getmsg = xmlobject.responseText
        'Print getmsg
        code = Json("code", getmsg)
        List2.AddItem code
        If code = "1" Then
            List1.AddItem "���ͽ�ˮָ��ɹ���"
        Else
            List1.AddItem "���ͽ�ˮָ��ʧ�ܣ�"
        End If
    End If
    Set xmlobject = Nothing
End Sub



Private Sub Command2_Click()
If Not begin Then
    Timer1.Enabled = Not begin   'ע��Timer�ؼ���enable�����ڳ�ʼ��״̬��Ϊfalse
    MsgBox ("��ʼ�������ݣ�")
    Command2.Caption = "ֹͣ����"
    begin = Not begin
Else
    Timer1.Enabled = Not begin
    MsgBox ("ֹͣ�������ݣ�")
    Command2.Caption = "��ʼ����"
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
        '���ַ����ķ�ʽ�ҳ�
        If getmsg <> oldstr And code = "1" Then
            searchchar1 = "Content"
            searchchar2 = "Created"
            charpos1 = InStr(1, getmsg, searchchar1, 1)
            charpos2 = InStr(1, getmsg, searchchar2, 1)
            val = Mid(getmsg, charpos1 + 10, charpos2 - 3 - charpos1 - 10)
            'Print val
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


