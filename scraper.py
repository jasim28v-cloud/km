#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  💙  GOMPBOOK 2009 - CLASSIC FACEBOOK STYLE  💙          ║
║     Ultimate Version - 10 Files - 2000+ Lines              ║
║                                                            ║
║  🔥  Firebase: gomp-99173                                 ║
║  ☁️   Cloudinary: dhu9l0lfs / f5_kmk                     ║
║  👑  Admin: jasim28v@gmail.com                            ║
║  👾  Avatars: DiceBear Big Smile (Random)                  ║
║  💙  Design: Facebook 2009 Classic Blue                   ║
║                                                            ║
║  ✨  FEATURES:                                             ║
║     • 📝 Wall Posts (Text + Images)                       ║
║     • 👫 Friends System                                   ║
║     • 💙 Like + Comment + Share                          ║
║     • 📸 Photo Albums                                    ║
║     • 💬 Messenger Chat                                   ║
║     • 🔔 Notifications                                   ║
║     • 👑 Admin Panel (Verify/Ban/Delete)                  ║
║     • 🛡️ Full Moderation                                 ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# 💙 CONFIGURATION - الإعدادات
# ═══════════════════════════════════════════════════════════

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyDpTq8zUxXLka0ey0I7eCcymynJGqmDw28",
    "authDomain": "gomp-99173.firebaseapp.com",
    "databaseURL": "https://gomp-99173-default-rtdb.firebaseio.com",
    "projectId": "gomp-99173",
    "storageBucket": "gomp-99173.firebasestorage.app",
    "messagingSenderId": "1070592379003",
    "appId": "1:1070592379003:web:d8fc4096902013e4a43ade",
    "measurementId": "G-MLJG2JYGF5"
}

CLOUD_NAME = "dhu9l0lfs"
UPLOAD_PRESET = "f5_kmk"
ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"

# 💙 Facebook 2009 Blue Palette
FB_BLUE = "#3b5998"
FB_BLUE_LIGHT = "#627aad"
FB_BLUE_DARK = "#1d2a4a"
FB_WHITE = "#ffffff"
FB_GRAY = "#f7f7f7"
FB_BORDER = "#d8dfea"

TOTAL_LINES = 0

def write(filename, content):
    """حفظ ملف وحساب عدد الأسطر"""
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    """طباعة عنوان القسم"""
    print(f"\n{'='*60}")
    print(f"  💙 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 💙 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 💙 GOMPBOOK 2009 - Classic Facebook Configuration
// Firebase: gomp-99173 | Cloudinary: dhu9l0lfs

const firebaseConfig = {{
    apiKey: "{FIREBASE_CONFIG['apiKey']}",
    authDomain: "{FIREBASE_CONFIG['authDomain']}",
    databaseURL: "{FIREBASE_CONFIG['databaseURL']}",
    projectId: "{FIREBASE_CONFIG['projectId']}",
    storageBucket: "{FIREBASE_CONFIG['storageBucket']}",
    messagingSenderId: "{FIREBASE_CONFIG['messagingSenderId']}",
    appId: "{FIREBASE_CONFIG['appId']}",
    measurementId: "{FIREBASE_CONFIG['measurementId']}"
}};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";

// 💙 GOMPBOOK Settings
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const FB_BLUE = "{FB_BLUE}";
const FB_BLUE_LIGHT = "{FB_BLUE_LIGHT}";

// 💙 App Info
const APP_NAME = "GOMPBOOK";
const APP_VERSION = "2009.1";

console.log('💙 %c'+APP_NAME+' '+APP_VERSION+' Ready', 'color: #3b5998; font-size: 18px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# 💙 2. auth.html - تسجيل دخول فيسبوك 2009
# ═══════════════════════════════════════════════════════════

def build_auth():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💙 GOMPBOOK | تسجيل الدخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
            background:#e9ebee;
            min-height:100vh;
        }
        .header{
            background:#3b5998;
            color:white;
            padding:12px 0;
            box-shadow:0 2px 4px rgba(0,0,0,0.1);
        }
        .header-inner{
            max-width:980px;
            margin:0 auto;
            padding:0 20px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }
        .logo{
            font-size:32px;
            font-weight:bold;
            letter-spacing:-1px;
            color:white;
            text-decoration:none;
        }
        .login-form-top{
            display:flex;
            gap:8px;
            align-items:center;
            font-size:12px;
        }
        .login-form-top input{
            padding:5px 8px;
            border:1px solid #1d2a4a;
            border-radius:2px;
            font-size:12px;
            width:140px;
        }
        .login-form-top button{
            background:#5b74a8;
            color:white;
            border:1px solid #29447e;
            padding:4px 10px;
            cursor:pointer;
            font-weight:bold;
            font-size:12px;
            border-radius:2px;
        }
        .login-form-top button:hover{background:#4a6491}
        .login-form-top a{color:#9cb4d8;text-decoration:none;font-size:11px}

        .main-content{
            max-width:980px;
            margin:0 auto;
            padding:30px 20px;
            display:flex;
            gap:60px;
        }
        .info-section{
            flex:1;
            padding-top:30px;
        }
        .info-section h2{
            font-size:20px;
            color:#333;
            margin-bottom:12px;
            font-weight:normal;
        }
        .info-section p{
            color:#666;
            font-size:14px;
            line-height:1.6;
        }
        .signup-section{
            flex:1;
        }
        .signup-box{
            background:white;
            padding:20px;
            border-radius:4px;
            box-shadow:0 1px 3px rgba(0,0,0,0.1);
        }
        .signup-box h2{
            font-size:28px;
            color:#333;
            margin-bottom:8px;
        }
        .signup-box .subtitle{
            color:#666;
            font-size:14px;
            margin-bottom:16px;
        }
        .signup-box input{
            width:100%;
            padding:8px 10px;
            margin:6px 0;
            border:1px solid #bdc7d8;
            border-radius:4px;
            font-size:14px;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }
        .name-row{
            display:flex;
            gap:8px;
        }
        .name-row input{flex:1}
        .signup-box button{
            background:linear-gradient(#67ae55, #578843);
            color:white;
            border:1px solid #3b6e22;
            padding:8px 20px;
            font-size:16px;
            font-weight:bold;
            border-radius:4px;
            cursor:pointer;
            margin-top:10px;
            min-width:180px;
            box-shadow:inset 0 1px 1px #a4e388;
        }
        .signup-box button:hover{background:linear-gradient(#79bc64, #578843)}
        .signup-box button:disabled{opacity:0.6;cursor:not-allowed}
        .msg{color:#d93025;font-size:12px;margin-top:8px;min-height:18px}
        .msg.success{color:#4caf50}

        .footer{
            text-align:center;
            padding:20px;
            color:#999;
            font-size:11px;
            border-top:1px solid #ddd;
            margin-top:40px;
        }

        @media (max-width:768px){
            .main-content{flex-direction:column;gap:20px}
            .header-inner{flex-direction:column;gap:10px}
            .login-form-top{flex-wrap:wrap;justify-content:center}
        }
    </style>
</head>
<body>

<div class="header">
    <div class="header-inner">
        <a href="index.html" class="logo">gompbook</a>
        <form class="login-form-top" onsubmit="event.preventDefault();doLoginTop()">
            <div>
                <input type="email" id="loginEmailTop" placeholder="البريد الإلكتروني">
            </div>
            <div>
                <input type="password" id="loginPassTop" placeholder="كلمة المرور">
            </div>
            <button type="submit">دخول</button>
            <a href="#">نسيت كلمة السر؟</a>
        </form>
    </div>
</div>

<div class="main-content">
    <div class="info-section">
        <h2>GOMPBOOK يساعدك على التواصل ومشاركة ما تريد مع الأشخاص المهمين في حياتك.</h2>
        <p>💙 انضم إلى شبكة التواصل الاجتماعي الكلاسيكية. شارك منشوراتك، صورك، وتواصل مع أصدقائك بتصميم فيسبوك 2009 الأصلي.</p>
    </div>
    <div class="signup-section">
        <div class="signup-box">
            <h2>إنشاء حساب جديد</h2>
            <p class="subtitle">إنه مجاني وسيبقى مجانيًا دائمًا.</p>
            <div class="name-row">
                <input type="text" id="regName" placeholder="الاسم الكامل">
            </div>
            <input type="email" id="regEmail" placeholder="البريد الإلكتروني">
            <input type="password" id="regPass" placeholder="كلمة المرور">
            <button id="btnRegister" onclick="doRegister()">تسجيل الاشتراك</button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>
</div>

<div class="footer">💙 GOMPBOOK 2009 &copy; جميع الحقوق محفوظة</div>

<script src="firebase-config.js"></script>
<script>
    async function doLoginTop(){
        const email = document.getElementById('loginEmailTop').value.trim();
        const password = document.getElementById('loginPassTop').value;
        if(!email || !password){ alert('الرجاء ملء جميع الحقول'); return; }
        try {
            await auth.signInWithEmailAndPassword(email, password);
            window.location.replace('index.html');
        } catch(e) {
            alert('خطأ في تسجيل الدخول: ' + (e.message || 'غير معروف'));
        }
    }

    async function doRegister(){
        const username = document.getElementById('regName').value.trim();
        const email = document.getElementById('regEmail').value.trim();
        const password = document.getElementById('regPass').value;
        const msg = document.getElementById('regMsg');
        const btn = document.getElementById('btnRegister');
        if(!username || !email || !password){ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }
        if(username.length < 3){ msg.innerText = '❌ الاسم 3 أحرف على الأقل'; return; }
        if(password.length < 6){ msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل'; return; }
        btn.disabled = true; btn.innerText = 'جاري إنشاء الحساب...'; msg.innerText = ''; msg.className = 'msg';
        try {
            const userCredential = await auth.createUserWithEmailAndPassword(email, password);
            const uid = userCredential.user.uid;
            const avatarUrl = DICEBEAR_URL + '?seed=' + uid;
            const userData = {
                username: username, email: email, bio: '',
                website: '', location: '', contactEmail: '',
                avatarUrl: avatarUrl, hasCustomAvatar: false,
                coverImageUrl: '', hasCustomCover: false,
                friends: {}, friendRequests: {},
                totalLikes: 0, isVerified: false, verifiedAt: null, verifiedBy: null,
                banned: false, createdAt: Date.now(), lastSeen: Date.now()
            };
            await db.ref('users/' + uid).set(userData);
            msg.innerText = '✅ تم إنشاء الحساب بنجاح! جاري التوجيه...';
            msg.className = 'msg success';
            setTimeout(() => { window.location.replace('index.html'); }, 1000);
        } catch(error) {
            btn.disabled = false; btn.innerText = 'تسجيل الاشتراك'; msg.className = 'msg';
            switch(error.code) {
                case 'auth/email-already-in-use': msg.innerText = '❌ البريد الإلكتروني مستخدم بالفعل'; break;
                case 'auth/weak-password': msg.innerText = '❌ كلمة المرور ضعيفة جداً'; break;
                case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                default: msg.innerText = '❌ خطأ: ' + (error.message || 'غير معروف');
            }
        }
    }

    auth.onAuthStateChanged(user => {
        if(user) { window.location.replace('index.html'); }
    });

    document.querySelectorAll('input').forEach(input => {
        input.addEventListener('keydown', function(e) {
            if(e.key === 'Enter') {
                e.preventDefault();
                if(this.closest('.login-form-top')) doLoginTop();
                else doRegister();
            }
        });
    });

    console.log('💙 GOMPBOOK Auth Ready');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💙 3. index.html - الوول الرئيسي (فيسبوك 2009)
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>💙 GOMPBOOK | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
            background:#e9ebee;
            color:#333;
            min-height:100vh;
        }
        /* Facebook 2009 Top Bar */
        .fb-header{
            background:#3b5998;
            color:white;
            padding:0;
            position:fixed;
            top:0;left:0;right:0;
            z-index:1000;
            height:42px;
            box-shadow:0 2px 4px rgba(0,0,0,0.15);
        }
        .fb-header-inner{
            max-width:980px;
            margin:0 auto;
            display:flex;
            justify-content:space-between;
            align-items:center;
            height:100%;
            padding:0 10px;
        }
        .fb-logo{
            font-size:22px;
            font-weight:bold;
            color:white;
            text-decoration:none;
            margin-right:10px;
        }
        .fb-nav{
            display:flex;
            align-items:center;
            gap:15px;
        }
        .fb-nav a, .fb-nav button{
            color:white;
            text-decoration:none;
            font-size:12px;
            font-weight:bold;
            padding:6px 10px;
            border-radius:2px;
            transition:background 0.2s;
            background:none;
            border:none;
            cursor:pointer;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
            white-space:nowrap;
        }
        .fb-nav a:hover, .fb-nav button:hover{background:rgba(255,255,255,0.1)}
        .fb-nav .active{background:rgba(255,255,255,0.15)}
        .notif-dot{
            position:relative;
        }
        .notif-badge{
            position:absolute;top:-3px;left:-3px;
            background:#d93025;
            color:white;
            width:18px;height:18px;
            border-radius:50%;
            font-size:10px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:bold;
            display:none;
        }

        /* Main Layout */
        .main-container{
            max-width:980px;
            margin:52px auto 0;
            padding:10px;
            display:flex;
            gap:10px;
        }
        .sidebar-left{
            width:200px;
            flex-shrink:0;
        }
        .sidebar-left .section-title{
            font-size:12px;
            color:#666;
            font-weight:bold;
            margin-bottom:8px;
            padding:8px 10px;
            border-bottom:1px solid #ddd;
        }
        .sidebar-left a{
            display:flex;
            align-items:center;
            gap:8px;
            padding:6px 10px;
            color:#3b5998;
            text-decoration:none;
            font-size:12px;
            border-radius:2px;
            margin:2px 0;
        }
        .sidebar-left a:hover{background:#ddd}
        .sidebar-left a i{width:16px;text-align:center;color:#666}
        .content-area{
            flex:1;
            min-width:0;
        }
        .sidebar-right{
            width:200px;
            flex-shrink:0;
        }

        /* Post Composer */
        .composer{
            background:white;
            border:1px solid #ddd;
            border-radius:2px;
            padding:12px;
            margin-bottom:10px;
        }
        .composer-top{
            display:flex;
            gap:8px;
            align-items:center;
            margin-bottom:8px;
        }
        .composer-top img{
            width:40px;height:40px;border-radius:2px;object-fit:cover;
        }
        .composer-top input{
            flex:1;
            padding:8px 10px;
            border:1px solid #ddd;
            border-radius:2px;
            font-size:13px;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
            background:#f7f7f7;
        }
        .composer-btns{
            display:flex;
            gap:8px;
            border-top:1px solid #eee;
            padding-top:8px;
        }
        .composer-btn{
            flex:1;
            padding:6px;
            text-align:center;
            font-size:11px;
            font-weight:bold;
            color:#666;
            cursor:pointer;
            border-radius:2px;
            background:none;
            border:none;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }
        .composer-btn:hover{background:#f0f0f0}
        .composer-btn i{margin-left:4px;color:#3b5998}
        .composer-preview{
            margin-top:8px;
            position:relative;
            display:none;
        }
        .composer-preview img{
            max-width:100%;
            max-height:200px;
            border-radius:2px;
        }
        .composer-preview .remove-preview{
            position:absolute;
            top:4px;left:4px;
            background:rgba(0,0,0,0.6);
            color:white;
            width:24px;height:24px;
            border-radius:50%;
            display:flex;
            align-items:center;
            justify-content:center;
            cursor:pointer;
            font-size:14px;
            border:none;
        }
        .composer .btn-post{
            background:#3b5998;
            color:white;
            border:none;
            padding:8px 20px;
            border-radius:2px;
            font-weight:bold;
            font-size:12px;
            cursor:pointer;
            margin-top:8px;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }
        .composer .btn-post:hover{background:#4a6491}
        .composer textarea{
            width:100%;
            padding:8px;
            border:1px solid #ddd;
            border-radius:2px;
            font-size:13px;
            resize:vertical;
            min-height:60px;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
            margin-top:8px;
            display:none;
        }

        /* Post Card */
        .post{
            background:white;
            border:1px solid #ddd;
            border-radius:2px;
            padding:12px;
            margin-bottom:10px;
        }
        .post-header{
            display:flex;
            align-items:center;
            gap:8px;
            margin-bottom:8px;
        }
        .post-avatar{
            width:40px;height:40px;
            border-radius:2px;
            object-fit:cover;
            cursor:pointer;
        }
        .post-author{
            font-weight:bold;
            font-size:12px;
            color:#3b5998;
            cursor:pointer;
            text-decoration:none;
        }
        .post-author:hover{text-decoration:underline}
        .post-time{
            font-size:10px;
            color:#999;
        }
        .verified-badge{
            display:inline-flex;
            align-items:center;
            justify-content:center;
            width:14px;height:14px;
            background:#3b5998;
            color:white;
            border-radius:50%;
            font-size:8px;
            margin-right:3px;
            vertical-align:middle;
        }
        .post-text{
            font-size:13px;
            line-height:1.5;
            margin-bottom:8px;
            word-wrap:break-word;
        }
        .post-image{
            max-width:100%;
            border-radius:2px;
            cursor:pointer;
            margin-bottom:8px;
        }
        .post-actions{
            display:flex;
            border-top:1px solid #eee;
            padding-top:8px;
            gap:4px;
        }
        .post-action-btn{
            flex:1;
            padding:6px;
            text-align:center;
            font-size:11px;
            color:#666;
            cursor:pointer;
            border:none;
            background:none;
            border-radius:2px;
            font-weight:bold;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }
        .post-action-btn:hover{background:#eee}
        .post-action-btn.liked{color:#3b5998}
        .post-action-btn i{margin-left:3px}

        /* Comments */
        .post-comments{
            background:#f7f7f7;
            padding:8px;
            border-radius:2px;
            margin-top:8px;
        }
        .comment{
            display:flex;
            gap:6px;
            margin-bottom:6px;
            font-size:11px;
        }
        .comment img{
            width:28px;height:28px;border-radius:2px;flex-shrink:0;
        }
        .comment-body{
            background:white;
            padding:5px 8px;
            border-radius:0 8px 8px 8px;
            border:1px solid #eee;
        }
        .comment-author{
            font-weight:bold;
            color:#3b5998;
            font-size:10px;
        }
        .comment-input-row{
            display:flex;
            gap:6px;
            margin-top:8px;
        }
        .comment-input-row input{
            flex:1;
            padding:6px 10px;
            border:1px solid #ddd;
            border-radius:2px;
            font-size:11px;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }
        .comment-input-row button{
            background:#3b5998;
            color:white;
            border:none;
            padding:4px 10px;
            border-radius:2px;
            font-size:11px;
            cursor:pointer;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }

        /* Lightbox */
        .lightbox{
            position:fixed;inset:0;
            background:rgba(0,0,0,0.85);
            z-index:9999;
            display:flex;
            align-items:center;
            justify-content:center;
            opacity:0;pointer-events:none;
            transition:opacity 0.3s;
            flex-direction:column;
        }
        .lightbox.active{opacity:1;pointer-events:auto}
        .lightbox img{
            max-width:90vw;max-height:80vh;
            border-radius:4px;
            box-shadow:0 10px 40px rgba(0,0,0,0.5);
        }
        .lightbox-close{
            position:absolute;top:20px;left:20px;
            background:rgba(255,255,255,0.2);
            color:white;
            width:40px;height:40px;
            border-radius:50%;
            display:flex;
            align-items:center;
            justify-content:center;
            cursor:pointer;
            font-size:20px;
            border:none;
        }
        .lightbox-close:hover{background:rgba(255,255,255,0.3)}

        .spinner{
            width:30px;height:30px;
            border:3px solid #ddd;
            border-top-color:#3b5998;
            border-radius:50%;
            animation:spin 0.7s linear infinite;
            margin:20px auto;
        }
        @keyframes spin{to{transform:rotate(360deg)}}
        .empty-state{
            text-align:center;
            padding:40px;
            color:#999;
            font-size:13px;
        }
        .toast{
            position:fixed;bottom:20px;left:50%;transform:translateX(-50%);
            background:#333;color:white;
            padding:10px 24px;border-radius:4px;
            z-index:2000;opacity:0;transition:opacity 0.3s;
            pointer-events:none;font-size:12px;
        }
        .toast.show{opacity:1}

        @media (max-width:768px){
            .main-container{flex-direction:column}
            .sidebar-left{display:none}
            .sidebar-right{display:none}
            .fb-nav{gap:8px}
            .fb-nav a, .fb-nav button{font-size:10px;padding:4px 6px}
        }
    </style>
</head>
<body>

<div class="fb-header">
    <div class="fb-header-inner">
        <a href="index.html" class="fb-logo">gompbook</a>
        <div class="fb-nav">
            <a href="index.html" class="active"><i class="fas fa-home"></i> الرئيسية</a>
            <a href="profile.html"><i class="fas fa-user"></i> بروفايلي</a>
            <a href="friends.html"><i class="fas fa-users"></i> أصدقاء</a>
            <a href="chat.html"><i class="fas fa-comment"></i> رسائل</a>
            <button class="notif-dot" onclick="openNotifs()">
                <i class="fas fa-bell"></i>
                <span class="notif-badge" id="notifBadge"></span>
            </button>
            <button onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i></button>
        </div>
    </div>
</div>

<div class="main-container">
    <div class="sidebar-left">
        <div class="section-title">القائمة</div>
        <a href="index.html"><i class="fas fa-newspaper"></i> آخر الأخبار</a>
        <a href="chat.html"><i class="fas fa-envelope"></i> الرسائل</a>
        <a href="friends.html"><i class="fas fa-user-friends"></i> الأصدقاء</a>
        <a href="photos.html"><i class="fas fa-images"></i> الصور</a>
    </div>

    <div class="content-area">
        <!-- Composer -->
        <div class="composer" id="composer">
            <div class="composer-top">
                <img id="composerAvatar" src="" alt="me">
                <input type="text" id="composerInput" placeholder="بماذا تفكر؟" onfocus="showComposerFull()">
            </div>
            <textarea id="composerTextarea" placeholder="اكتب منشورك هنا..."></textarea>
            <div class="composer-preview" id="composerPreview">
                <img id="previewImg" src="" alt="preview">
                <button class="remove-preview" onclick="removePreview()">✕</button>
            </div>
            <input type="file" id="composerImageFile" accept="image/*" style="display:none" onchange="previewComposerImage(this)">
            <div class="composer-btns">
                <button class="composer-btn" onclick="document.getElementById('composerImageFile').click()"><i class="fas fa-image"></i> صورة</button>
            </div>
            <button class="btn-post" onclick="submitPost()">نشر</button>
        </div>

        <!-- Posts Feed -->
        <div id="postsFeed">
            <div class="spinner"></div>
        </div>
    </div>

    <div class="sidebar-right">
        <div class="section-title">آخر النشاطات</div>
        <div id="activitySidebar" style="font-size:11px;color:#666;padding:8px;">
            <div class="spinner"></div>
        </div>
    </div>
</div>

<!-- Lightbox -->
<div class="lightbox" id="lightbox" onclick="closeLightbox()">
    <button class="lightbox-close" onclick="closeLightbox()">✕</button>
    <img id="lightboxImg" src="" alt="صورة">
</div>

<div class="toast" id="toast"></div>

<script src="firebase-config.js"></script>
<script>
    let currentUser = null;
    let currentUserData = null;
    let allUsers = {};
    let allPosts = [];
    let selectedImageFile = null;

    // Lightbox
    function openLightbox(url) {
        document.getElementById('lightboxImg').src = url;
        document.getElementById('lightbox').classList.add('active');
    }
    function closeLightbox() {
        document.getElementById('lightbox').classList.remove('active');
        document.getElementById('lightboxImg').src = '';
    }

    // Composer
    function showComposerFull() {
        document.getElementById('composerTextarea').style.display = 'block';
        document.getElementById('composerTextarea').focus();
    }
    function previewComposerImage(input) {
        const file = input.files[0];
        if (!file) return;
        selectedImageFile = file;
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('previewImg').src = e.target.result;
            document.getElementById('composerPreview').style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
    function removePreview() {
        selectedImageFile = null;
        document.getElementById('composerPreview').style.display = 'none';
        document.getElementById('composerImageFile').value = '';
    }

    async function submitPost() {
        const textarea = document.getElementById('composerTextarea');
        const text = textarea.value.trim();
        if (!text && !selectedImageFile) { showToast('اكتب شيئاً أو أضف صورة'); return; }
        const btn = document.querySelector('.btn-post');
        btn.disabled = true; btn.innerText = 'جاري النشر...';
        try {
            let imageUrl = null;
            if (selectedImageFile) {
                const fd = new FormData();
                fd.append('file', selectedImageFile);
                fd.append('upload_preset', UPLOAD_PRESET);
                const res = await fetch('https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/image/upload', { method: 'POST', body: fd });
                const data = await res.json();
                if (data.secure_url) imageUrl = data.secure_url;
            }
            const postData = {
                text: text,
                imageUrl: imageUrl,
                authorId: currentUser.uid,
                authorName: currentUserData?.username || 'مستخدم',
                authorAvatar: currentUserData?.avatarUrl || (DICEBEAR_URL + '?seed=' + currentUser.uid),
                likes: {},
                comments: {},
                timestamp: Date.now()
            };
            await db.ref('posts').push(postData);
            // Notify friends
            const friends = currentUserData?.friends || {};
            for (let friendId in friends) {
                await db.ref('notifications/' + friendId).push({
                    from: currentUserData?.username,
                    msg: 'أضاف منشوراً جديداً',
                    timestamp: Date.now(),
                    read: false,
                    type: 'new_post',
                    postAuthorId: currentUser.uid
                });
            }
            textarea.value = '';
            textarea.style.display = 'none';
            removePreview();
            showToast('✅ تم نشر المنشور');
            loadPosts();
        } catch(e) {
            showToast('❌ حدث خطأ');
            console.error(e);
        }
        btn.disabled = false; btn.innerText = 'نشر';
    }

    // Posts
    function loadPosts() {
        const feed = document.getElementById('postsFeed');
        if (!allPosts.length) {
            feed.innerHTML = '<div class="empty-state"><i class="fas fa-newspaper" style="font-size:48px;color:#ddd;display:block;margin-bottom:10px;"></i>لا توجد منشورات بعد. كن أول من ينشر!</div>';
            return;
        }
        const sorted = allPosts.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
        feed.innerHTML = sorted.map(post => {
            const author = allUsers[post.authorId] || { username: post.authorName || 'مستخدم', avatarUrl: post.authorAvatar };
            const isLiked = post.likes && post.likes[currentUser?.uid];
            const likesCount = post.likes ? Object.keys(post.likes).length : 0;
            const commentsCount = post.comments ? Object.keys(post.comments).length : 0;
            const verifiedBadge = author.isVerified ? '<span class="verified-badge"><i class="fas fa-check"></i></span>' : '';
            const timeAgo = formatTimeAgo(post.timestamp);

            let commentsHtml = '';
            if (post.comments) {
                const commentsArr = Object.entries(post.comments).sort(([,a],[,b]) => (a.timestamp || 0) - (b.timestamp || 0)).slice(-5);
                commentsHtml = commentsArr.map(([cid, c]) => {
                    const cu = allUsers[c.userId] || { username: c.username || 'مستخدم', avatarUrl: DICEBEAR_URL + '?seed=' + (c.userId || 'unknown') };
                    return `<div class="comment">
                        <img src="${cu.avatarUrl || (DICEBEAR_URL + '?seed=' + c.userId)}" alt="avatar">
                        <div class="comment-body">
                            <span class="comment-author">${cu.username}</span>
                            ${c.text}
                        </div>
                    </div>`;
                }).join('');
            }

            return `<div class="post">
                <div class="post-header">
                    <img src="${author.avatarUrl || (DICEBEAR_URL + '?seed=' + post.authorId)}" class="post-avatar" onclick="openProfile('${post.authorId}')">
                    <div>
                        <a class="post-author" onclick="openProfile('${post.authorId}')">${author.username} ${verifiedBadge}</a>
                        <div class="post-time">${timeAgo}</div>
                    </div>
                </div>
                ${post.text ? `<div class="post-text">${escapeHtml(post.text)}</div>` : ''}
                ${post.imageUrl ? `<img src="${post.imageUrl}" class="post-image" onclick="openLightbox('${post.imageUrl}')" loading="lazy">` : ''}
                <div class="post-actions">
                    <button class="post-action-btn ${isLiked ? 'liked' : ''}" onclick="toggleLike('${post.id}', this)">
                        <i class="fas fa-thumbs-up"></i> إعجاب (${likesCount})
                    </button>
                    <button class="post-action-btn" onclick="focusComment('${post.id}')">
                        <i class="fas fa-comment"></i> تعليق (${commentsCount})
                    </button>
                    <button class="post-action-btn" onclick="sharePost('${post.id}')">
                        <i class="fas fa-share"></i> مشاركة
                    </button>
                </div>
                ${post.comments ? `<div class="post-comments">${commentsHtml}</div>` : ''}
                <div class="comment-input-row">
                    <input type="text" id="commentInput_${post.id}" placeholder="اكتب تعليقاً..." onkeydown="if(event.key==='Enter')addComment('${post.id}')">
                    <button onclick="addComment('${post.id}')">تعليق</button>
                </div>
            </div>`;
        }).join('');
    }

    async function toggleLike(postId, btn) {
        if (!currentUser) return;
        const ref = db.ref('posts/' + postId);
        const snap = await ref.get();
        const post = snap.val();
        if (!post) return;
        let likes = post.likes || {};
        if (likes[currentUser.uid]) {
            delete likes[currentUser.uid];
        } else {
            likes[currentUser.uid] = true;
            if (post.authorId && post.authorId !== currentUser.uid) {
                await db.ref('notifications/' + post.authorId).push({
                    from: currentUserData?.username,
                    msg: 'أعجب بمنشورك 👍',
                    timestamp: Date.now(),
                    read: false,
                    type: 'like',
                    postId: postId
                });
            }
        }
        await ref.update({ likes });
        btn.classList.toggle('liked');
        const countMatch = btn.innerText.match(/\((\d+)\)/);
        if (countMatch) {
            const newCount = likes[currentUser.uid] ? parseInt(countMatch[1]) + 1 : parseInt(countMatch[1]) - 1;
            btn.innerHTML = `<i class="fas fa-thumbs-up"></i> إعجاب (${Math.max(0, newCount)})`;
        }
    }

    function focusComment(postId) {
        const input = document.getElementById('commentInput_' + postId);
        if (input) input.focus();
    }

    async function addComment(postId) {
        const input = document.getElementById('commentInput_' + postId);
        if (!input || !input.value.trim()) return;
        const commentData = {
            userId: currentUser.uid,
            username: currentUserData?.username || 'مستخدم',
            text: input.value.trim(),
            timestamp: Date.now()
        };
        await db.ref('posts/' + postId + '/comments').push(commentData);
        const postSnap = await db.ref('posts/' + postId).get();
        const post = postSnap.val();
        if (post && post.authorId !== currentUser.uid) {
            await db.ref('notifications/' + post.authorId).push({
                from: currentUserData?.username,
                msg: 'علّق على منشورك 💬',
                timestamp: Date.now(),
                read: false,
                type: 'comment',
                postId: postId
            });
        }
        input.value = '';
        loadPosts();
    }

    function sharePost(postId) {
        const url = window.location.origin + '/index.html?post=' + postId;
        if (navigator.share) {
            navigator.share({ title: 'منشور من GOMPBOOK', url: url }).catch(() => {});
        } else {
            navigator.clipboard.writeText(url).then(() => showToast('✅ تم نسخ الرابط'));
        }
    }

    // Notifications
    async function openNotifs() {
        const snap = await db.ref('notifications/' + currentUser.uid).once('value');
        const ns = snap.val() || {};
        const items = Object.values(ns).reverse();
        let notifText = items.length ? items.map(n => `🔔 ${n.from || 'مستخدم'}: ${n.msg} - ${formatTimeAgo(n.timestamp)}`).join('\\n') : 'لا توجد إشعارات';
        alert('🔔 الإشعارات:\\n\\n' + notifText);
        await db.ref('notifications/' + currentUser.uid).remove();
        updateNotifBadge();
    }

    function updateNotifBadge() {
        const badge = document.getElementById('notifBadge');
        if (badge) badge.style.display = 'none';
    }

    // Helpers
    function openProfile(uid) {
        if (uid === currentUser?.uid) { window.location.href = 'profile.html'; }
        else { window.location.href = 'profile.html?uid=' + uid; }
    }
    function showToast(msg) {
        const toast = document.getElementById('toast');
        toast.innerText = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2000);
    }
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.innerText = text;
        return div.innerHTML.replace(/#(\w+)/g, '<span style="color:#3b5998;cursor:pointer">#$1</span>');
    }
    function formatTimeAgo(ts) {
        if (!ts) return '';
        const diff = Date.now() - ts;
        const mins = Math.floor(diff / 60000);
        const hours = Math.floor(diff / 3600000);
        const days = Math.floor(diff / 86400000);
        if (mins < 1) return 'الآن';
        if (mins < 60) return 'منذ ' + mins + ' دقيقة';
        if (hours < 24) return 'منذ ' + hours + ' ساعة';
        if (days < 7) return 'منذ ' + days + ' يوم';
        return new Date(ts).toLocaleDateString('ar-SA');
    }

    // Init
    auth.onAuthStateChanged(async (user) => {
        if (!user) { window.location.replace('auth.html'); return; }
        currentUser = user;
        const snap = await db.ref('users/' + user.uid).get();
        if (snap.exists()) currentUserData = { uid: user.uid, ...snap.val() };

        // Set composer avatar
        document.getElementById('composerAvatar').src = currentUserData?.avatarUrl || (DICEBEAR_URL + '?seed=' + user.uid);

        // Load users
        db.ref('users').on('value', s => { allUsers = s.val() || {}; });

        // Load posts
        db.ref('posts').on('value', s => {
            const data = s.val();
            if (!data) { allPosts = []; }
            else {
                allPosts = Object.entries(data).map(([key, value]) => ({ id: key, ...value }));
            }
            loadPosts();
        });

        // Listen for new notifications
        db.ref('notifications/' + user.uid).on('value', s => {
            const ns = s.val() || {};
            const badge = document.getElementById('notifBadge');
            if (badge) {
                const count = Object.keys(ns).length;
                if (count > 0) {
                    badge.style.display = 'flex';
                    badge.innerText = count;
                } else {
                    badge.style.display = 'none';
                }
            }
        });

        // Update last seen
        db.ref('users/' + user.uid + '/lastSeen').set(Date.now());
        setInterval(() => {
            if (currentUser) db.ref('users/' + currentUser.uid + '/lastSeen').set(Date.now());
        }, 60000);
    });

    console.log('💙 GOMPBOOK Wall Ready');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💙 4. profile.html - بروفايل فيسبوك 2009
# ═══════════════════════════════════════════════════════════

def build_profile():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💙 GOMPBOOK | بروفايل</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
            background:#e9ebee;
            color:#333;
            min-height:100vh;
        }
        .fb-header{
            background:#3b5998;
            color:white;
            position:fixed;
            top:0;left:0;right:0;
            z-index:1000;
            height:42px;
            box-shadow:0 2px 4px rgba(0,0,0,0.15);
        }
        .fb-header-inner{
            max-width:980px;
            margin:0 auto;
            display:flex;
            justify-content:space-between;
            align-items:center;
            height:100%;
            padding:0 10px;
        }
        .fb-logo{
            font-size:22px;
            font-weight:bold;
            color:white;
            text-decoration:none;
        }
        .fb-nav a, .fb-nav button{
            color:white;
            text-decoration:none;
            font-size:12px;
            font-weight:bold;
            padding:6px 10px;
            border-radius:2px;
            background:none;
            border:none;
            cursor:pointer;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }
        .fb-nav a:hover, .fb-nav button:hover{background:rgba(255,255,255,0.1)}

        .cover-wrap{
            background:#3b5998;
            height:200px;
            position:relative;
            margin-top:42px;
            overflow:hidden;
        }
        .cover-wrap img{
            width:100%;
            height:100%;
            object-fit:cover;
        }
        .cover-gradient{
            position:absolute;
            bottom:0;left:0;right:0;
            height:80px;
            background:linear-gradient(transparent, rgba(0,0,0,0.3));
        }

        .profile-main{
            max-width:980px;
            margin:0 auto;
            padding:0 10px;
            position:relative;
        }
        .avatar-section{
            display:flex;
            align-items:flex-end;
            gap:12px;
            margin-top:-60px;
            position:relative;
            z-index:2;
        }
        .avatar-lg{
            width:120px;
            height:120px;
            border:4px solid white;
            border-radius:4px;
            object-fit:cover;
            background:white;
            box-shadow:0 1px 3px rgba(0,0,0,0.2);
        }
        .profile-name-section{
            flex:1;
            padding-bottom:10px;
        }
        .profile-name{
            font-size:22px;
            font-weight:bold;
            color:white;
            text-shadow:0 1px 3px rgba(0,0,0,0.5);
        }
        .verified-badge{
            display:inline-flex;
            align-items:center;
            justify-content:center;
            width:18px;height:18px;
            background:#3b5998;
            color:white;
            border-radius:50%;
            font-size:10px;
            vertical-align:middle;
            margin-right:4px;
        }

        .profile-nav{
            border-bottom:1px solid #ddd;
            background:white;
            padding:0 10px;
            margin-bottom:10px;
        }
        .profile-nav-inner{
            max-width:980px;
            margin:0 auto;
            display:flex;
            gap:0;
        }
        .profile-tab{
            padding:12px 16px;
            font-size:12px;
            font-weight:bold;
            color:#666;
            cursor:pointer;
            border-bottom:3px solid transparent;
            background:none;
            border-top:none;
            border-left:none;
            border-right:none;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }
        .profile-tab.active{
            color:#3b5998;
            border-bottom-color:#3b5998;
        }
        .profile-tab:hover{background:#f7f7f7}

        .content-grid{
            max-width:980px;
            margin:0 auto;
            padding:10px;
            display:flex;
            gap:10px;
        }
        .left-col{width:280px;flex-shrink:0}
        .right-col{flex:1;min-width:0}

        .info-box{
            background:white;
            border:1px solid #ddd;
            border-radius:2px;
            padding:12px;
            margin-bottom:10px;
        }
        .info-box h4{
            font-size:12px;
            color:#333;
            margin-bottom:8px;
            border-bottom:1px solid #eee;
            padding-bottom:6px;
        }
        .info-row{
            font-size:11px;
            color:#666;
            margin:4px 0;
            display:flex;
            align-items:center;
            gap:6px;
        }
        .info-row i{width:16px;text-align:center;color:#999}

        .friends-grid{
            display:grid;
            grid-template-columns:repeat(3,1fr);
            gap:4px;
            margin-top:8px;
        }
        .friend-mini{
            text-align:center;
            cursor:pointer;
        }
        .friend-mini img{
            width:50px;height:50px;
            object-fit:cover;
            border-radius:2px;
        }
        .friend-mini span{
            font-size:9px;
            color:#3b5998;
            display:block;
            margin-top:2px;
        }

        .btn-friend{
            background:#3b5998;
            color:white;
            border:none;
            padding:8px 16px;
            border-radius:2px;
            font-weight:bold;
            font-size:12px;
            cursor:pointer;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
            margin:4px 0;
        }
        .btn-friend:hover{background:#4a6491}
        .btn-friend.pending{background:#90949c}
        .btn-friend.friends{background:#42b72a}
        .btn-friend.friends:hover{background:#36a420}
        .btn-edit{
            background:#f0f0f0;
            border:1px solid #ccc;
            padding:6px 14px;
            border-radius:2px;
            font-size:12px;
            cursor:pointer;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }

        /* Admin Panel */
        .admin-box{
            background:white;
            border:2px solid #3b5998;
            border-radius:4px;
            padding:16px;
            margin-bottom:10px;
        }
        .admin-box h3{
            color:#3b5998;
            margin-bottom:12px;
            font-size:14px;
        }
        .admin-stats{
            display:grid;
            grid-template-columns:repeat(2,1fr);
            gap:8px;
            margin-bottom:12px;
        }
        .stat-card{
            background:#f7f7f7;
            padding:10px;
            border-radius:4px;
            text-align:center;
        }
        .stat-card .stat-val{
            font-size:24px;
            font-weight:bold;
            color:#3b5998;
        }
        .stat-card .stat-lbl{
            font-size:10px;
            color:#666;
        }
        .admin-btn{
            background:#3b5998;
            color:white;
            border:none;
            padding:6px 12px;
            border-radius:2px;
            font-size:11px;
            cursor:pointer;
            margin:2px;
            font-family:'lucida grande',tahoma,verdana,arial,sans-serif;
        }
        .admin-btn.ban{background:#d93025}
        .admin-btn.ban:hover{background:#b71c1c}
        .admin-btn:hover{background:#4a6491}

        .spinner{
            width:30px;height:30px;
            border:3px solid #ddd;
            border-top-color:#3b5998;
            border-radius:50%;
            animation:spin 0.7s linear infinite;
            margin:20px auto;
        }
        @keyframes spin{to{transform:rotate(360deg)}}
        .toast{
            position:fixed;bottom:20px;left:50%;transform:translateX(-50%);
            background:#333;color:white;
            padding:10px 24px;border-radius:4px;
            z-index:2000;opacity:0;transition:opacity 0.3s;
            pointer-events:none;font-size:12px;
        }
        .toast.show{opacity:1}

        @media (max-width:768px){
            .content-grid{flex-direction:column}
            .left-col{width:100%}
            .avatar-lg{width:80px;height:80px}
            .profile-name{font-size:16px}
        }
    </style>
</head>
<body>

<div class="fb-header">
    <div class="fb-header-inner">
        <a href="index.html" class="fb-logo">gompbook</a>
        <div class="fb-nav">
            <a href="index.html">الرئيسية</a>
            <a href="profile.html" class="active">بروفايلي</a>
            <a href="friends.html">أصدقاء</a>
            <a href="chat.html">رسائل</a>
            <button onclick="auth.signOut();window.location.href='auth.html'">خروج</button>
        </div>
    </div>
</div>

<div class="cover-wrap" id="coverWrap">
    <img id="coverImg" src="" alt="cover" style="display:none">
    <div class="cover-gradient"></div>
</div>

<div class="profile-main">
    <div class="avatar-section">
        <img id="avatarImg" class="avatar-lg" src="" alt="avatar">
        <div class="profile-name-section">
            <div class="profile-name">
                <span id="nameDisplay"></span>
            </div>
        </div>
    </div>
</div>

<div class="profile-nav">
    <div class="profile-nav-inner">
        <button class="profile-tab active" onclick="switchTab('wall', this)">الحائط</button>
        <button class="profile-tab" onclick="switchTab('info', this)">معلومات</button>
        <button class="profile-tab" onclick="switchTab('photos', this)">صور</button>
        <button class="profile-tab" onclick="switchTab('friends', this)">أصدقاء</button>
    </div>
</div>

<div class="content-grid">
    <div class="left-col">
        <div class="info-box" id="infoBox">
            <h4>معلومات</h4>
            <div id="infoContent"><div class="spinner"></div></div>
        </div>
        <div class="info-box" id="friendsBox">
            <h4>الأصدقاء (<span id="friendsCount">0</span>)</h4>
            <div class="friends-grid" id="friendsGrid"></div>
        </div>
        <div id="actionsBox"></div>
    </div>
    <div class="right-col" id="mainContent">
        <div class="spinner"></div>
    </div>
</div>

<div class="toast" id="toast"></div>

<script src="firebase-config.js"></script>
<script>
    let currentUser = null;
    let currentUserData = null;
    let profileUserId = null;
    let isOwnProfile = false;
    let allUsers = {};
    let allPosts = [];
    let currentTab = 'wall';

    function switchTab(tab, btn) {
        currentTab = tab;
        document.querySelectorAll('.profile-tab').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
        loadMainContent();
    }

    function loadMainContent() {
        const mc = document.getElementById('mainContent');
        if (currentTab === 'wall') {
            loadWallPosts();
        } else if (currentTab === 'info') {
            loadDetailedInfo();
        } else if (currentTab === 'photos') {
            loadPhotos();
        } else if (currentTab === 'friends') {
            loadFriendsFull();
        }
    }

    function loadWallPosts() {
        const mc = document.getElementById('mainContent');
        const userPosts = allPosts.filter(p => p.authorId === profileUserId).sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
        if (!userPosts.length) {
            mc.innerHTML = '<div style="background:white;border:1px solid #ddd;padding:20px;text-align:center;color:#999;">لا توجد منشورات على الحائط</div>';
            return;
        }
        mc.innerHTML = userPosts.map(post => {
            const author = allUsers[post.authorId] || { username: post.authorName };
            return `<div style="background:white;border:1px solid #ddd;padding:12px;margin-bottom:8px;">
                <div style="font-weight:bold;font-size:12px;color:#3b5998;margin-bottom:4px;">${author.username}</div>
                ${post.text ? `<div style="font-size:13px;margin-bottom:6px;">${post.text}</div>` : ''}
                ${post.imageUrl ? `<img src="${post.imageUrl}" style="max-width:100%;cursor:pointer" onclick="window.open('${post.imageUrl}')">` : ''}
                <div style="font-size:10px;color:#999;margin-top:4px;">❤️ ${Object.keys(post.likes||{}).length} إعجاب | 💬 ${Object.keys(post.comments||{}).length} تعليق</div>
            </div>`;
        }).join('');
    }

    function loadDetailedInfo() {
        const mc = document.getElementById('mainContent');
        const u = allUsers[profileUserId];
        if (!u) { mc.innerHTML = '<div style="text-align:center;padding:40px;">لا توجد معلومات</div>'; return; }
        mc.innerHTML = `<div style="background:white;border:1px solid #ddd;padding:16px;">
            <h4 style="color:#333;margin-bottom:12px;">معلومات أساسية</h4>
            <p><strong>الاسم:</strong> ${u.username || ''}</p>
            <p><strong>البريد:</strong> ${u.email || ''}</p>
            <p><strong>السيرة:</strong> ${u.bio || 'لا توجد'}</p>
            <p><strong>الموقع:</strong> ${u.location || 'غير محدد'}</p>
            <p><strong>آخر ظهور:</strong> ${formatTimeAgo(u.lastSeen)}</p>
            <p><strong>تاريخ الانضمام:</strong> ${new Date(u.createdAt).toLocaleDateString('ar-SA')}</p>
        </div>`;
    }

    function loadPhotos() {
        const mc = document.getElementById('mainContent');
        const userPosts = allPosts.filter(p => p.authorId === profileUserId && p.imageUrl);
        if (!userPosts.length) {
            mc.innerHTML = '<div style="background:white;border:1px solid #ddd;padding:20px;text-align:center;color:#999;">لا توجد صور</div>';
            return;
        }
        mc.innerHTML = `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;">${userPosts.map(p => `<img src="${p.imageUrl}" style="width:100%;aspect-ratio:1;object-fit:cover;cursor:pointer;" onclick="window.open('${p.imageUrl}')">`).join('')}</div>`;
    }

    function loadFriendsFull() {
        const mc = document.getElementById('mainContent');
        const u = allUsers[profileUserId];
        const friends = u?.friends || {};
        const friendIds = Object.keys(friends);
        if (!friendIds.length) {
            mc.innerHTML = '<div style="background:white;border:1px solid #ddd;padding:20px;text-align:center;color:#999;">لا يوجد أصدقاء بعد</div>';
            return;
        }
        mc.innerHTML = `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;">${friendIds.map(fid => {
            const fu = allUsers[fid] || { username: 'مستخدم' };
            return `<div style="background:white;border:1px solid #ddd;padding:8px;text-align:center;cursor:pointer;" onclick="openProfile('${fid}')">
                <img src="${fu.avatarUrl || (DICEBEAR_URL + '?seed=' + fid)}" style="width:60px;height:60px;object-fit:cover;border-radius:2px;margin-bottom:4px;">
                <div style="font-size:11px;color:#3b5998;">${fu.username}</div>
            </div>`;
        }).join('')}</div>`;
    }

    async function loadProfile() {
        const u = allUsers[profileUserId];
        if (!u) {
            document.body.innerHTML = '<div style="text-align:center;padding:80px;font-size:18px;">المستخدم غير موجود</div>';
            return;
        }
        const verifiedBadge = u.isVerified ? '<span class="verified-badge"><i class="fas fa-check"></i></span>' : '';
        document.getElementById('nameDisplay').innerHTML = u.username + ' ' + verifiedBadge;
        document.getElementById('avatarImg').src = u.avatarUrl || (DICEBEAR_URL + '?seed=' + profileUserId);

        // Cover
        if (u.coverImageUrl) {
            document.getElementById('coverImg').src = u.coverImageUrl;
            document.getElementById('coverImg').style.display = 'block';
        }

        // Info Box
        document.getElementById('infoContent').innerHTML = `
            <div class="info-row"><i class="fas fa-user"></i> ${u.username}</div>
            ${u.bio ? `<div class="info-row"><i class="fas fa-quote-right"></i> ${u.bio}</div>` : ''}
            ${u.location ? `<div class="info-row"><i class="fas fa-map-marker-alt"></i> ${u.location}</div>` : ''}
            <div class="info-row"><i class="fas fa-clock"></i> آخر ظهور: ${formatTimeAgo(u.lastSeen)}</div>
        `;

        // Friends Box
        const friends = u.friends || {};
        const friendIds = Object.keys(friends).slice(0, 6);
        document.getElementById('friendsCount').innerText = Object.keys(friends).length;
        document.getElementById('friendsGrid').innerHTML = friendIds.map(fid => {
            const fu = allUsers[fid] || { username: 'مستخدم' };
            return `<div class="friend-mini" onclick="openProfile('${fid}')">
                <img src="${fu.avatarUrl || (DICEBEAR_URL + '?seed=' + fid)}" alt="friend">
                <span>${fu.username.substring(0, 8)}</span>
            </div>`;
        }).join('') || '<span style="font-size:10px;color:#999;">لا يوجد أصدقاء</span>';

        // Actions
        const actionsBox = document.getElementById('actionsBox');
        if (isOwnProfile) {
            actionsBox.innerHTML = `<button class="btn-edit" onclick="editProfile()">تعديل الملف</button>`;
        } else {
            const isFriend = currentUserData?.friends?.[profileUserId];
            const hasRequest = u.friendRequests?.[currentUser?.uid];
            let btnClass = 'btn-friend';
            let btnText = 'أضف صديقاً';
            let btnAction = 'sendFriendRequest()';
            if (isFriend) {
                btnClass += ' friends';
                btnText = '✓ صديق';
                btnAction = 'removeFriend()';
            } else if (hasRequest) {
                btnClass += ' pending';
                btnText = 'تم إرسال الطلب';
                btnAction = '';
            }
            actionsBox.innerHTML = `
                <button class="${btnClass}" onclick="${btnAction}" ${!btnAction ? 'disabled' : ''}>${btnText}</button>
                <button class="btn-edit" onclick="window.location.href='chat.html?uid=${profileUserId}'">مراسلة</button>
            `;
        }

        // Admin Panel
        if (isOwnProfile && ADMIN_EMAILS.includes(currentUser?.email)) {
            loadAdminPanel();
        }

        loadMainContent();
    }

    async function sendFriendRequest() {
        await db.ref('users/' + profileUserId + '/friendRequests/' + currentUser.uid).set({
            username: currentUserData?.username,
            avatarUrl: currentUserData?.avatarUrl,
            timestamp: Date.now()
        });
        await db.ref('notifications/' + profileUserId).push({
            from: currentUserData?.username,
            msg: 'أرسل لك طلب صداقة 👫',
            timestamp: Date.now(),
            type: 'friend_request',
            fromUserId: currentUser.uid
        });
        showToast('✅ تم إرسال طلب الصداقة');
        loadProfile();
    }

    async function removeFriend() {
        if (!confirm('إزالة من الأصدقاء؟')) return;
        await db.ref('users/' + currentUser.uid + '/friends/' + profileUserId).remove();
        await db.ref('users/' + profileUserId + '/friends/' + currentUser.uid).remove();
        showToast('تمت إزالة الصديق');
        loadProfile();
    }

    async function editProfile() {
        const u = allUsers[profileUserId] || currentUserData;
        const newUsername = prompt('الاسم الجديد:', u?.username || '');
        if (newUsername && newUsername.trim().length >= 3) {
            await db.ref('users/' + profileUserId).update({ username: newUsername.trim() });
            showToast('✅ تم تحديث الاسم');
            location.reload();
        }
    }

    function openProfile(uid) {
        if (uid === currentUser?.uid) { window.location.href = 'profile.html'; }
        else { window.location.href = 'profile.html?uid=' + uid; }
    }

    // Admin
    async function loadAdminPanel() {
        const mc = document.getElementById('mainContent');
        const totalUsers = Object.keys(allUsers).length;
        const totalPosts = allPosts.length;
        const totalBanned = Object.values(allUsers).filter(u => u.banned).length;
        const totalVerified = Object.values(allUsers).filter(u => u.isVerified).length;

        const adminHtml = `<div class="admin-box">
            <h3>👑 لوحة تحكم الأدمن</h3>
            <div class="admin-stats">
                <div class="stat-card"><div class="stat-val">${totalUsers}</div><div class="stat-lbl">مستخدمين</div></div>
                <div class="stat-card"><div class="stat-val">${totalPosts}</div><div class="stat-lbl">منشورات</div></div>
                <div class="stat-card"><div class="stat-val">${totalBanned}</div><div class="stat-lbl">محظورين</div></div>
                <div class="stat-card"><div class="stat-val">${totalVerified}</div><div class="stat-lbl">موثقين</div></div>
            </div>
            <h4 style="margin:8px 0;">قائمة المستخدمين (أحدث 10)</h4>
            <div id="adminUserList"></div>
            <h4 style="margin:8px 0;">أحدث المنشورات</h4>
            <div id="adminPostList"></div>
        </div>`;

        const existingAdmin = document.getElementById('adminPanelContainer');
        if (existingAdmin) existingAdmin.remove();

        const adminDiv = document.createElement('div');
        adminDiv.id = 'adminPanelContainer';
        adminDiv.innerHTML = adminHtml;
        mc.prepend(adminDiv);

        // Load admin lists
        const userList = document.getElementById('adminUserList');
        const usersArr = Object.entries(allUsers).sort(([,a],[,b]) => (b.createdAt||0) - (a.createdAt||0)).slice(0, 10);
        userList.innerHTML = usersArr.map(([id, u]) => `
            <div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid #eee;font-size:11px;">
                <span style="cursor:pointer;color:#3b5998;" onclick="openProfile('${id}')">${u.username || 'مستخدم'} ${u.isVerified?'✓':''}</span>
                <span>
                    <button class="admin-btn" onclick="toggleVerify('${id}')">${u.isVerified?'إلغاء توثيق':'توثيق'}</button>
                    <button class="admin-btn ban" onclick="toggleBan('${id}')">${u.banned?'إلغاء حظر':'حظر'}</button>
                    <button class="admin-btn ban" onclick="deleteUserPosts('${id}')">حذف منشورات</button>
                </span>
            </div>
        `).join('');

        const postList = document.getElementById('adminPostList');
        const postsArr = allPosts.sort((a,b) => (b.timestamp||0) - (a.timestamp||0)).slice(0, 10);
        postList.innerHTML = postsArr.map(p => `
            <div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid #eee;font-size:11px;">
                <span>${(p.text || 'صورة').substring(0, 30)} - ${p.authorName || 'مستخدم'}</span>
                <button class="admin-btn ban" onclick="deletePost('${p.id}')">حذف</button>
            </div>
        `).join('');
    }

    window.toggleVerify = async function(id) {
        const u = allUsers[id];
        await db.ref('users/' + id).update({ isVerified: !u.isVerified, verifiedAt: Date.now(), verifiedBy: currentUser.uid });
        showToast('✅ تم');
        setTimeout(() => location.reload(), 500);
    };
    window.toggleBan = async function(id) {
        const u = allUsers[id];
        await db.ref('users/' + id).update({ banned: !u.banned, bannedAt: Date.now(), bannedBy: currentUser.uid });
        showToast('✅ تم');
        setTimeout(() => location.reload(), 500);
    };
    window.deletePost = async function(postId) {
        if (!confirm('حذف المنشور؟')) return;
        await db.ref('posts/' + postId).remove();
        showToast('🗑️ تم حذف المنشور');
        setTimeout(() => location.reload(), 500);
    };
    window.deleteUserPosts = async function(userId) {
        if (!confirm('حذف جميع منشورات هذا المستخدم؟')) return;
        const userPosts = allPosts.filter(p => p.authorId === userId);
        for (let p of userPosts) {
            await db.ref('posts/' + p.id).remove();
        }
        showToast('🗑️ تم حذف جميع المنشورات');
        setTimeout(() => location.reload(), 500);
    };

    function showToast(msg) {
        const toast = document.getElementById('toast');
        toast.innerText = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2000);
    }
    function formatTimeAgo(ts) {
        if (!ts) return '';
        const diff = Date.now() - ts;
        const mins = Math.floor(diff / 60000);
        if (mins < 1) return 'الآن';
        if (mins < 60) return 'منذ ' + mins + ' دقيقة';
        const hours = Math.floor(diff / 3600000);
        if (hours < 24) return 'منذ ' + hours + ' ساعة';
        return new Date(ts).toLocaleDateString('ar-SA');
    }

    // Init
    auth.onAuthStateChanged(async (user) => {
        if (!user) { window.location.replace('auth.html'); return; }
        currentUser = user;
        const params = new URLSearchParams(window.location.search);
        profileUserId = params.get('uid') || user.uid;
        isOwnProfile = (profileUserId === user.uid);

        const snap = await db.ref('users/' + user.uid).get();
        if (snap.exists()) currentUserData = { uid: user.uid, ...snap.val() };

        db.ref('users').on('value', s => {
            allUsers = s.val() || {};
            loadProfile();
        });

        db.ref('posts').on('value', s => {
            const data = s.val();
            allPosts = data ? Object.entries(data).map(([k, v]) => ({ id: k, ...v })) : [];
            if (currentTab === 'wall') loadWallPosts();
            if (currentTab === 'photos') loadPhotos();
        });

        db.ref('users/' + user.uid + '/lastSeen').set(Date.now());
        setInterval(() => {
            if (currentUser) db.ref('users/' + currentUser.uid + '/lastSeen').set(Date.now());
        }, 60000);
    });

    console.log('💙 GOMPBOOK Profile Ready');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💙 5-10. الملفات المتبقية
# ═══════════════════════════════════════════════════════════

def build_upload():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💙 GOMPBOOK | منشور جديد</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'lucida grande',tahoma,verdana,arial,sans-serif;background:#e9ebee;color:#333;min-height:100vh}
        .fb-header{background:#3b5998;color:white;padding:0;height:42px;box-shadow:0 2px 4px rgba(0,0,0,0.15);display:flex;align-items:center;padding:0 10px}
        .fb-logo{font-size:22px;font-weight:bold;color:white;text-decoration:none}
        .container{max-width:600px;margin:20px auto;padding:10px}
        .post-box{background:white;border:1px solid #ddd;border-radius:2px;padding:20px}
        .post-box h2{font-size:14px;color:#333;margin-bottom:12px;border-bottom:1px solid #eee;padding-bottom:8px}
        .post-box textarea{width:100%;min-height:100px;padding:10px;border:1px solid #ddd;border-radius:2px;font-size:13px;resize:vertical;font-family:'lucida grande',tahoma,verdana,arial,sans-serif;margin-bottom:10px}
        .post-box input[type="file"]{margin:8px 0;font-size:12px}
        .preview-img{max-width:100%;max-height:200px;border-radius:2px;margin:8px 0;display:none}
        .btn-post{background:#3b5998;color:white;border:none;padding:10px 24px;border-radius:2px;font-weight:bold;font-size:13px;cursor:pointer;font-family:'lucida grande',tahoma,verdana,arial,sans-serif}
        .btn-post:hover{background:#4a6491}
        .btn-post:disabled{opacity:0.6}
        .toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#333;color:white;padding:10px 24px;border-radius:4px;z-index:2000;opacity:0;transition:opacity 0.3s;pointer-events:none;font-size:12px}
        .toast.show{opacity:1}
        .spinner{width:30px;height:30px;border:3px solid #ddd;border-top-color:#3b5998;border-radius:50%;animation:spin 0.7s linear infinite;margin:10px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div class="fb-header"><a href="index.html" class="fb-logo">gompbook</a></div>
<div class="container">
    <div class="post-box">
        <h2>إنشاء منشور جديد</h2>
        <textarea id="postText" placeholder="بماذا تفكر؟"></textarea>
        <input type="file" id="postImage" accept="image/*" onchange="previewImage(this)">
        <img id="preview" class="preview-img" src="" alt="معاينة">
        <button class="btn-post" onclick="submitPost()">نشر</button>
        <div id="uploadProgress" style="display:none;"><div class="spinner"></div><p style="text-align:center;font-size:11px;color:#666;">جاري رفع الصورة...</p></div>
        <div id="status" style="text-align:center;margin-top:8px;font-size:12px;"></div>
    </div>
</div>
<div class="toast" id="toast"></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()}});
    function previewImage(i){const f=i.files[0];if(!f)return;const r=new FileReader();r.onload=e=>{const p=document.getElementById('preview');p.src=e.target.result;p.style.display='block'};r.readAsDataURL(f)}
    async function submitPost(){
        const text=document.getElementById('postText').value.trim();
        const imgInput=document.getElementById('postImage');
        const file=imgInput.files[0];
        if(!text && !file){showToast('اكتب شيئاً أو أضف صورة');return}
        const btn=document.querySelector('.btn-post');btn.disabled=true;btn.innerText='جاري النشر...';
        document.getElementById('uploadProgress').style.display='block';
        let imageUrl=null;
        if(file){
            const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);
            const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});
            const data=await res.json();
            if(data.secure_url)imageUrl=data.secure_url;
        }
        await db.ref('posts').push({text,imageUrl,authorId:currentUser.uid,authorName:currentUserData?.username,authorAvatar:currentUserData?.avatarUrl,likes:{},comments:{},timestamp:Date.now()});
        document.getElementById('uploadProgress').style.display='none';
        showToast('✅ تم نشر المنشور!');
        setTimeout(()=>window.location.href='index.html',1000);
    }
    function showToast(msg){const t=document.getElementById('toast');t.innerText=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2000)}
</script>
</body>
</html>"""

def build_chat():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💙 GOMPBOOK | رسائل</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'lucida grande',tahoma,verdana,arial,sans-serif;background:#e9ebee;color:#333;height:100vh;display:flex;flex-direction:column}
        .fb-header{background:#3b5998;color:white;padding:0;height:42px;display:flex;align-items:center;padding:0 10px;box-shadow:0 2px 4px rgba(0,0,0,0.15)}
        .fb-logo{font-size:22px;font-weight:bold;color:white;text-decoration:none;margin-left:10px}
        .btn-back{background:none;border:none;color:white;cursor:pointer;font-size:16px}
        .conv-list{flex:1;overflow-y:auto;background:white;border-left:1px solid #ddd;max-width:300px}
        .conv-item{display:flex;align-items:center;gap:10px;padding:10px 12px;border-bottom:1px solid #eee;cursor:pointer}
        .conv-item:hover{background:#f0f0f0}
        .conv-avatar{width:36px;height:36px;border-radius:2px;object-fit:cover}
        .conv-name{font-size:12px;font-weight:bold;color:#3b5998}
        .chat-area{flex:1;display:flex;flex-direction:column;background:white}
        .chat-header{padding:10px;border-bottom:1px solid #ddd;font-weight:bold;font-size:13px;display:flex;align-items:center;gap:8px}
        .msgs{flex:1;overflow-y:auto;padding:10px;display:flex;flex-direction:column;gap:6px}
        .bubble{max-width:70%;padding:8px 12px;border-radius:12px;font-size:12px;word-break:break-word}
        .bubble.sent{background:#3b5998;color:white;align-self:flex-end;border-radius:12px 12px 0 12px}
        .bubble.received{background:#f0f0f0;color:#333;align-self:flex-start;border-radius:12px 12px 12px 0}
        .bubble img{max-width:150px;border-radius:4px;cursor:pointer;margin-top:4px}
        .input-bar{display:flex;gap:8px;padding:10px;border-top:1px solid #ddd;background:#f7f7f7}
        .input-bar input{flex:1;padding:8px 12px;border:1px solid #ddd;border-radius:16px;font-size:12px;font-family:'lucida grande',tahoma,verdana,arial,sans-serif}
        .input-bar button{background:#3b5998;color:white;border:none;padding:8px 16px;border-radius:16px;font-size:12px;cursor:pointer;font-family:'lucida grande',tahoma,verdana,arial,sans-serif}
        .spinner{width:24px;height:24px;border:3px solid #ddd;border-top-color:#3b5998;border-radius:50%;animation:spin 0.7s linear infinite;margin:15px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#333;color:white;padding:10px 24px;border-radius:4px;z-index:2000;opacity:0;transition:opacity 0.3s;pointer-events:none;font-size:12px}
        .toast.show{opacity:1}
    </style>
</head>
<body>
<div class="fb-header"><a href="index.html" class="fb-logo">gompbook</a></div>
<div style="display:flex;flex:1;overflow:hidden">
    <div class="conv-list" id="convList"><div class="spinner"></div></div>
    <div class="chat-area" id="chatArea"><div style="flex:1;display:flex;align-items:center;justify-content:center;color:#999;font-size:13px">اختر محادثة</div></div>
</div>
<div class="toast" id="toast"></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,allUsers={},chatUserId=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const us=await db.ref('users').once('value');allUsers=us.val()||{};loadConvs();const params=new URLSearchParams(window.location.search);const target=params.get('uid');if(target)openChat(target)});
    async function loadConvs(){const cl=document.getElementById('convList');cl.innerHTML='<div class="spinner"></div>';const snap=await db.ref('private_messages').once('value');const all=snap.val()||{};const found=new Set();Object.keys(all).forEach(cid=>{const[u1,u2]=cid.split('_');const other=u1===currentUser.uid?u2:u2===currentUser.uid?u1:null;if(other&&!found.has(other)&&allUsers[other])found.add(other)});if(!found.size){cl.innerHTML='<div style="text-align:center;padding:20px;color:#999;font-size:12px;">لا توجد محادثات</div>';return}cl.innerHTML=Array.from(found).map(uid=>{const u=allUsers[uid];return`<div class="conv-item" onclick="openChat('${uid}')"><img src="${u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}" class="conv-avatar"><div class="conv-name">${u?.username||'مستخدم'}</div></div>`}).join('')}
    function openChat(uid){chatUserId=uid;const u=allUsers[uid];const ca=document.getElementById('chatArea');ca.innerHTML=`<div class="chat-header"><img src="${u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}" style="width:28px;height:28px;border-radius:2px;"><span>${u?.username||'مستخدم'}</span></div><div class="msgs" id="msgsList"><div class="spinner"></div></div><div class="input-bar"><input type="text" id="msgInput" placeholder="اكتب رسالة..." onkeydown="if(event.key==='Enter')sendMsg()"><button onclick="sendMsg()">إرسال</button></div>`;loadMsgs()}
    function getChatId(){return[currentUser.uid,chatUserId].sort().join('_')}
    async function loadMsgs(){const ml=document.getElementById('msgsList');if(!ml)return;const snap=await db.ref('private_messages/'+getChatId()).once('value');const ms=snap.val()||{};ml.innerHTML=Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).map(m=>{const sent=m.senderId===currentUser.uid;return`<div class="bubble ${sent?'sent':'received'}">${m.type==='image'?`<img src="${m.imageUrl}" onclick="window.open('${m.imageUrl}')">`:m.text}</div>`}).join('');ml.scrollTop=ml.scrollHeight}
    async function sendMsg(){const inp=document.getElementById('msgInput');if(!inp)return;const txt=inp.value.trim();if(!txt||!chatUserId)return;await db.ref('private_messages/'+getChatId()).push({senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()});inp.value='';await loadMsgs()}
    function showToast(msg){const t=document.getElementById('toast');t.innerText=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2000)}
</script>
</body>
</html>"""

def build_friends():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💙 GOMPBOOK | الأصدقاء</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'lucida grande',tahoma,verdana,arial,sans-serif;background:#e9ebee;color:#333;min-height:100vh}
        .fb-header{background:#3b5998;color:white;padding:0;height:42px;display:flex;align-items:center;padding:0 10px;box-shadow:0 2px 4px rgba(0,0,0,0.15)}
        .fb-logo{font-size:22px;font-weight:bold;color:white;text-decoration:none}
        .container{max-width:800px;margin:20px auto;padding:10px}
        .tabs{display:flex;gap:0;background:white;border:1px solid #ddd;border-radius:2px 2px 0 0;overflow:hidden}
        .tab-btn{flex:1;padding:10px;border:none;background:white;font-size:12px;font-weight:bold;color:#666;cursor:pointer;font-family:'lucida grande',tahoma,verdana,arial,sans-serif}
        .tab-btn.active{color:#3b5998;border-bottom:2px solid #3b5998;background:#f7f7f7}
        .list-box{background:white;border:1px solid #ddd;border-top:none;border-radius:0 0 2px 2px;min-height:300px}
        .user-row{display:flex;align-items:center;justify-content:space-between;padding:10px;border-bottom:1px solid #eee}
        .user-row:hover{background:#f7f7f7}
        .user-info{display:flex;align-items:center;gap:10px;cursor:pointer}
        .user-info img{width:40px;height:40px;border-radius:2px;object-fit:cover}
        .user-name{font-size:13px;font-weight:bold;color:#3b5998}
        .btn{background:#3b5998;color:white;border:none;padding:6px 14px;border-radius:2px;font-size:11px;font-weight:bold;cursor:pointer;font-family:'lucida grande',tahoma,verdana,arial,sans-serif}
        .btn:hover{background:#4a6491}
        .btn.green{background:#42b72a}
        .btn.gray{background:#90949c}
        .btn.red{background:#d93025}
        .spinner{width:30px;height:30px;border:3px solid #ddd;border-top-color:#3b5998;border-radius:50%;animation:spin 0.7s linear infinite;margin:20px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .empty-state{text-align:center;padding:40px;color:#999}
        .toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#333;color:white;padding:10px 24px;border-radius:4px;z-index:2000;opacity:0;transition:opacity 0.3s;pointer-events:none;font-size:12px}
        .toast.show{opacity:1}
    </style>
</head>
<body>
<div class="fb-header"><a href="index.html" class="fb-logo">gompbook</a></div>
<div class="container">
    <div class="tabs">
        <button class="tab-btn active" onclick="switchTab('myFriends', this)">أصدقائي</button>
        <button class="tab-btn" onclick="switchTab('requests', this)">طلبات الصداقة</button>
        <button class="tab-btn" onclick="switchTab('search', this)">بحث عن أصدقاء</button>
    </div>
    <div class="list-box" id="listContent"><div class="spinner"></div></div>
</div>
<div class="toast" id="toast"></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,allUsers={},currentTab='myFriends';
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()};db.ref('users').on('value',s=>{allUsers=s.val()||{};loadTab()})});
    function switchTab(tab,btn){currentTab=tab;document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));btn.classList.add('active');loadTab()}
    function loadTab(){const lc=document.getElementById('listContent');if(currentTab==='myFriends')loadMyFriends();else if(currentTab==='requests')loadRequests();else if(currentTab==='search')loadSearch()}
    function loadMyFriends(){const lc=document.getElementById('listContent');const friends=currentUserData?.friends||{};const ids=Object.keys(friends);if(!ids.length){lc.innerHTML='<div class="empty-state"><i class="fas fa-user-friends" style="font-size:40px;display:block;margin-bottom:10px;color:#ddd;"></i>لا يوجد أصدقاء بعد</div>';return}lc.innerHTML=ids.map(id=>{const u=allUsers[id]||{username:'مستخدم'};return`<div class="user-row"><div class="user-info" onclick="openProfile('${id}')"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+id)}"><span class="user-name">${u.username}</span></div><button class="btn red" onclick="removeFriend('${id}')">إزالة</button></div>`}).join('')}
    async function removeFriend(id){if(!confirm('إزالة من الأصدقاء؟'))return;await db.ref('users/'+currentUser.uid+'/friends/'+id).remove();await db.ref('users/'+id+'/friends/'+currentUser.uid).remove();showToast('تمت إزالة الصديق');setTimeout(()=>location.reload(),500)}
    function loadRequests(){const lc=document.getElementById('listContent');const requests=currentUserData?.friendRequests||{};const ids=Object.keys(requests);if(!ids.length){lc.innerHTML='<div class="empty-state"><i class="fas fa-user-plus" style="font-size:40px;display:block;margin-bottom:10px;color:#ddd;"></i>لا توجد طلبات صداقة</div>';return}lc.innerHTML=ids.map(id=>{const r=requests[id]||{};return`<div class="user-row"><div class="user-info" onclick="openProfile('${id}')"><img src="${r.avatarUrl||(DICEBEAR_URL+'?seed='+id)}"><span class="user-name">${r.username||'مستخدم'}</span></div><div style="display:flex;gap:6px"><button class="btn green" onclick="acceptFriend('${id}')">قبول</button><button class="btn gray" onclick="rejectFriend('${id}')">رفض</button></div></div>`}).join('')}
    async function acceptFriend(id){await db.ref('users/'+currentUser.uid+'/friends/'+id).set(true);await db.ref('users/'+id+'/friends/'+currentUser.uid).set(true);await db.ref('users/'+currentUser.uid+'/friendRequests/'+id).remove();showToast('✅ تم قبول الصداقة!');setTimeout(()=>location.reload(),500)}
    async function rejectFriend(id){await db.ref('users/'+currentUser.uid+'/friendRequests/'+id).remove();showToast('تم رفض الطلب');setTimeout(()=>location.reload(),500)}
    function loadSearch(){const lc=document.getElementById('listContent');lc.innerHTML=`<div style="padding:10px"><input type="text" id="searchInput" placeholder="ابحث عن مستخدمين..." onkeyup="doSearch()" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:2px;font-size:12px;font-family:'lucida grande',tahoma,verdana,arial,sans-serif"><div id="searchResults" style="margin-top:10px"></div></div>`}
    window.doSearch=function(){const q=document.getElementById('searchInput').value.toLowerCase();const sr=document.getElementById('searchResults');if(!q){sr.innerHTML='';return}const results=Object.entries(allUsers).filter(([id,u])=>u.username?.toLowerCase().includes(q)&&id!==currentUser?.uid).slice(0,20);if(!results.length){sr.innerHTML='<div class="empty-state">لا توجد نتائج</div>';return}sr.innerHTML=results.map(([id,u])=>{const isFriend=currentUserData?.friends?.[id];return`<div class="user-row"><div class="user-info" onclick="openProfile('${id}')"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+id)}"><span class="user-name">${u.username}</span></div>${isFriend?`<button class="btn green" disabled>✓ صديق</button>`:`<button class="btn" onclick="sendRequest('${id}')">أضف صديقاً</button>`}</div>`}).join('')}
    async function sendRequest(id){await db.ref('users/'+id+'/friendRequests/'+currentUser.uid).set({username:currentUserData?.username,avatarUrl:currentUserData?.avatarUrl,timestamp:Date.now()});showToast('✅ تم إرسال طلب الصداقة')}
    function openProfile(uid){if(uid===currentUser?.uid){window.location.href='profile.html'}else{window.location.href='profile.html?uid='+uid}}
    function showToast(msg){const t=document.getElementById('toast');t.innerText=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2000)}
</script>
</body>
</html>"""

def build_photos():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💙 GOMPBOOK | الصور</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'lucida grande',tahoma,verdana,arial,sans-serif;background:#e9ebee;color:#333;min-height:100vh}
        .fb-header{background:#3b5998;color:white;padding:0;height:42px;display:flex;align-items:center;padding:0 10px;box-shadow:0 2px 4px rgba(0,0,0,0.15)}
        .fb-logo{font-size:22px;font-weight:bold;color:white;text-decoration:none}
        .container{max-width:900px;margin:20px auto;padding:10px}
        .photos-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}
        .photos-grid img{width:100%;aspect-ratio:1;object-fit:cover;cursor:pointer;border-radius:2px;transition:opacity 0.2s}
        .photos-grid img:hover{opacity:0.9}
        .spinner{width:30px;height:30px;border:3px solid #ddd;border-top-color:#3b5998;border-radius:50%;animation:spin 0.7s linear infinite;margin:20px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .empty-state{text-align:center;padding:40px;color:#999;grid-column:1/-1}
        .lightbox{position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:9999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity 0.3s}
        .lightbox.active{opacity:1;pointer-events:auto}
        .lightbox img{max-width:90vw;max-height:80vh;border-radius:4px;box-shadow:0 10px 40px rgba(0,0,0,0.5)}
        .lightbox-close{position:absolute;top:20px;left:20px;background:rgba(255,255,255,0.2);color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;border:none}
    </style>
</head>
<body>
<div class="fb-header"><a href="index.html" class="fb-logo">gompbook</a></div>
<div class="container"><div class="photos-grid" id="photosGrid"><div class="spinner" style="grid-column:1/-1"></div></div></div>
<div class="lightbox" id="lightbox" onclick="closeLightbox()"><button class="lightbox-close" onclick="closeLightbox()">✕</button><img id="lightboxImg" src=""></div>
<script src="firebase-config.js"></script>
<script>
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}const snap=await db.ref('posts').once('value');const posts=snap.val()||{};const allPosts=Object.entries(posts).map(([k,v])=>({id:k,...v}));const imgPosts=allPosts.filter(p=>p.imageUrl).sort((a,b)=>(b.timestamp||0)-(a.timestamp||0));const pg=document.getElementById('photosGrid');if(!imgPosts.length){pg.innerHTML='<div class="empty-state"><i class="fas fa-images" style="font-size:48px;display:block;margin-bottom:10px;color:#ddd;"></i>لا توجد صور</div>';return}pg.innerHTML=imgPosts.map(p=>`<img src="${p.imageUrl}" onclick="openLightbox('${p.imageUrl}')" loading="lazy">`).join('')});
    function openLightbox(url){document.getElementById('lightboxImg').src=url;document.getElementById('lightbox').classList.add('active')}
    function closeLightbox(){document.getElementById('lightbox').classList.remove('active')}
</script>
</body>
</html>"""

def build_notifications():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💙 GOMPBOOK | إشعارات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'lucida grande',tahoma,verdana,arial,sans-serif;background:#e9ebee;color:#333;min-height:100vh}
        .fb-header{background:#3b5998;color:white;padding:0;height:42px;display:flex;align-items:center;padding:0 10px;box-shadow:0 2px 4px rgba(0,0,0,0.15)}
        .fb-logo{font-size:22px;font-weight:bold;color:white;text-decoration:none}
        .container{max-width:600px;margin:20px auto;padding:10px}
        .notif-card{background:white;border:1px solid #ddd;border-radius:2px;padding:10px 14px;margin-bottom:6px;display:flex;align-items:center;gap:10px;font-size:12px}
        .notif-card i{color:#3b5998;font-size:18px;width:24px;text-align:center}
        .notif-time{font-size:10px;color:#999}
        .empty-state{text-align:center;padding:40px;color:#999}
        .spinner{width:30px;height:30px;border:3px solid #ddd;border-top-color:#3b5998;border-radius:50%;animation:spin 0.7s linear infinite;margin:20px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div class="fb-header"><a href="index.html" class="fb-logo">gompbook</a></div>
<div class="container" id="notifList"><div class="spinner"></div></div>
<script src="firebase-config.js"></script>
<script>
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}const snap=await db.ref('notifications/'+u.uid).once('value');const ns=snap.val()||{};const items=Object.values(ns).reverse();const nl=document.getElementById('notifList');if(!items.length){nl.innerHTML='<div class="empty-state"><i class="fas fa-bell" style="font-size:48px;display:block;margin-bottom:10px;color:#ddd;"></i>لا توجد إشعارات</div>';return}nl.innerHTML=items.map(n=>{const icon=n.type==='friend_request'?'fa-user-plus':n.type==='like'?'fa-thumbs-up':'fa-bell';const time=n.timestamp?new Date(n.timestamp).toLocaleString('ar-SA'):'';return`<div class="notif-card"><i class="fas ${icon}"></i><div><div>${n.from||'مستخدم'}: ${n.msg||''}</div><div class="notif-time">${time}</div></div></div>`}).join('')});
</script>
</body>
</html>"""

def build_settings():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💙 GOMPBOOK | إعدادات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'lucida grande',tahoma,verdana,arial,sans-serif;background:#e9ebee;color:#333;min-height:100vh}
        .fb-header{background:#3b5998;color:white;padding:0;height:42px;display:flex;align-items:center;padding:0 10px;box-shadow:0 2px 4px rgba(0,0,0,0.15)}
        .fb-logo{font-size:22px;font-weight:bold;color:white;text-decoration:none}
        .container{max-width:600px;margin:20px auto;padding:10px}
        .settings-box{background:white;border:1px solid #ddd;border-radius:2px;padding:16px}
        .setting-item{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #eee;cursor:pointer;font-size:12px}
        .setting-item:hover{background:#f7f7f7;margin:0 -16px;padding:10px 16px}
        .setting-item i{color:#3b5998;width:20px;text-align:center;margin-left:8px}
        .btn-logout{background:#d93025;color:white;border:none;padding:10px 20px;border-radius:2px;font-weight:bold;font-size:12px;cursor:pointer;margin-top:16px;width:100%;font-family:'lucida grande',tahoma,verdana,arial,sans-serif}
        .btn-logout:hover{background:#b71c1c}
    </style>
</head>
<body>
<div class="fb-header"><a href="index.html" class="fb-logo">gompbook</a></div>
<div class="container">
    <div class="settings-box">
        <h3 style="margin-bottom:12px;color:#3b5998;">الإعدادات</h3>
        <div class="setting-item" onclick="window.location.href='profile.html'"><span><i class="fas fa-user"></i> الملف الشخصي</span><i class="fas fa-chevron-left"></i></div>
        <div class="setting-item" onclick="window.location.href='friends.html'"><span><i class="fas fa-users"></i> الأصدقاء</span><i class="fas fa-chevron-left"></i></div>
        <div class="setting-item"><span><i class="fas fa-globe"></i> اللغة: العربية</span></div>
        <div class="setting-item"><span><i class="fas fa-info-circle"></i> GOMPBOOK 2009.1</span></div>
        <button class="btn-logout" onclick="if(confirm('تسجيل الخروج؟')){auth.signOut();window.location.href='auth.html'}"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button>
    </div>
</div>
<script src="firebase-config.js"></script>
<script>auth.onAuthStateChanged(u=>{if(!u)window.location.href='auth.html'})</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💙 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  💙  GOMPBOOK 2009 - FACEBOOK CLASSIC STYLE  ✨       ║
║     Ultimate Generator - 10 Files - 2000+ Lines          ║
║                                                          ║
║  👫 Friends + 📝 Wall + 💬 Messenger + 👑 Admin       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("BUILDING GOMPBOOK 2009 FILES")
    
    write("firebase-config.js", build_config())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("profile.html", build_profile())
    write("upload.html", build_upload())
    write("chat.html", build_chat())
    write("friends.html", build_friends())
    write("photos.html", build_photos())
    write("notifications.html", build_notifications())
    write("settings.html", build_settings())
    
    print(f"""
{'='*60}
  💙 GOMPBOOK 2009 BUILD COMPLETE! ✨
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • 10 ملفات تم إنشاؤها

  📁 الملفات:
     1. firebase-config.js   → إعدادات Firebase + Cloudinary
     2. auth.html            → تسجيل دخول فيسبوك 2009
     3. index.html           → الوول الرئيسي + صندوق النشر
     4. profile.html         → بروفايل + حائط + لوحة أدمن
     5. upload.html          → إنشاء منشور جديد
     6. chat.html            → ماسنجر
     7. friends.html         → الأصدقاء + طلبات الصداقة + بحث
     8. photos.html          → معرض الصور
     9. notifications.html   → الإشعارات
     10. settings.html       → الإعدادات

  💙 مميزات فيسبوك 2009:
     • 🟦 أزرق كلاسيك #3b5998
     • 📝 منشورات نصية + صور
     • 👫 نظام أصدقاء كامل (إضافة/قبول/رفض/إزالة)
     • 👍 إعجاب + 💬 تعليق + 📤 مشاركة
     • 💬 ماسنجر خاص
     • 📸 معرض صور
     • 🔔 إشعارات
     • 👑 لوحة أدمن (توثيق/حظر/حذف منشورات)
     • 🛡️ إدارة كاملة للمحتوى والمستخدمين

  🔑 بيانات الاتصال:
     • Firebase: gomp-99173
     • Cloudinary: dhu9l0lfs / f5_kmk
     • Admin: jasim28v@gmail.com

  💙 للتشغيل: شغّل python gompbook.py وبعدها افتح auth.html
  💙 GOMPBOOK 2009 READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
