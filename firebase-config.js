// 💙 GOMPBOOK 2009 - Classic Facebook Configuration
// Firebase: gomp-99173 | Cloudinary: dhu9l0lfs

const firebaseConfig = {
    apiKey: "AIzaSyDpTq8zUxXLka0ey0I7eCcymynJGqmDw28",
    authDomain: "gomp-99173.firebaseapp.com",
    databaseURL: "https://gomp-99173-default-rtdb.firebaseio.com",
    projectId: "gomp-99173",
    storageBucket: "gomp-99173.firebasestorage.app",
    messagingSenderId: "1070592379003",
    appId: "1:1070592379003:web:d8fc4096902013e4a43ade",
    measurementId: "G-MLJG2JYGF5"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "dhu9l0lfs";
const UPLOAD_PRESET = "f5_kmk";

// 💙 GOMPBOOK Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const FB_BLUE = "#3b5998";
const FB_BLUE_LIGHT = "#627aad";

// 💙 App Info
const APP_NAME = "GOMPBOOK";
const APP_VERSION = "2009.1";

console.log('💙 %c'+APP_NAME+' '+APP_VERSION+' Ready', 'color: #3b5998; font-size: 18px; font-weight: bold;');
