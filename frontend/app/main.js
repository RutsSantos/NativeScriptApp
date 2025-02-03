// // app/main.js
// import Vue from 'nativescript-vue';
// import Home from './components/Home.vue';
// import Login from './components/Login.vue';
// import Facturacion from './components/Facturacion.vue';
// import { createStore } from 'vuex';
// import { createApp } from 'nativescript-vue';
// import { FirebaseMessaging } from '@nativescript/firebase-messaging';

// const store = createStore({
//     state: {
//         user: null,
//         invoices: [],
//         isProcessing: false
//     },
//     mutations: {
//         setUser(state, user) {
//             state.user = user;
//         },
//         setInvoices(state, invoices) {
//             state.invoices = invoices;
//         },
//         setProcessing(state, status) {
//             state.isProcessing = status;
//         }
//     },
//     actions: {
//         async login({ commit }, credentials) {
//             let response = await fetch('https://api.example.com/login', {
//                 method: 'POST',
//                 headers: { 'Content-Type': 'application/json' },
//                 body: JSON.stringify(credentials)
//             });
//             let data = await response.json();
//             commit('setUser', data.user);
//         },
//         async fetchInvoices({ commit }) {
//             let response = await fetch('https://api.example.com/invoices');
//             let data = await response.json();
//             commit('setInvoices', data);
//         },
//         async processInvoice({ commit }, invoiceData) {
//             commit('setProcessing', true);
//             await new Promise(resolve => setTimeout(resolve, 3000)); // Simulación de procesamiento en hilo separado
//             let response = await fetch('https://api.example.com/invoices', {
//                 method: 'POST',
//                 headers: { 'Content-Type': 'application/json' },
//                 body: JSON.stringify(invoiceData)
//             });
//             let data = await response.json();
//             commit('setInvoices', [...state.invoices, data]);
//             commit('setProcessing', false);
//         }
//     }
// });

// FirebaseMessaging.init().then(() => {
//     console.log("Firebase Messaging Initialized");
// }).catch(err => console.log("Firebase Init Error: ", err));

// createApp(Login).use(store).start();


import { createApp } from "nativescript-vue";
import App from "./App.vue";
import { registerPushNotifications } from "./services/firebase";

registerPushNotifications();

createApp(App).start();
