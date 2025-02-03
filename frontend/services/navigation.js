import Vue from "nativescript-vue";

export function navigateTo(componentName) {
    Vue.navigateTo(require(`@/components/${componentName}.vue`).default);
}
