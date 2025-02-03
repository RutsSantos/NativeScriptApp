<!-- <template>
    <Page>
        <ActionBar title="Login" />
        <StackLayout>
            <TextField v-model="credentials.email" hint="Correo electrónico" keyboardType="email" />
            <TextField v-model="credentials.password" hint="Contraseña" secure="true" />
            <Button text="Iniciar sesión" @tap="handleLogin" />
        </StackLayout>
    </Page>
</template>

<script>
import { mapActions } from 'vuex';

export default {
    data() {
        return {
            credentials: { email: '', password: '' }
        };
    },
    methods: {
        ...mapActions(['login']),
        async handleLogin() {
            await this.login(this.credentials);
            this.$navigateTo(require('./Home.vue'));
        }
    }
};
</script> -->



<template>
    <Page>
        <ActionBar title="Login" />
        <StackLayout>
            <TextField v-model="email" hint="Correo electrónico" />
            <TextField v-model="password" hint="Contraseña" secure="true" />
            <Button text="Iniciar sesión" @tap="login" />
        </StackLayout>
    </Page>
</template>

<script>
import { navigateTo } from "@/services/navigation";

export default {
    data() {
        return {
            email: "",
            password: "",
        };
    },
    methods: {
        login() {
            if (this.email && this.password) {
                navigateTo("Home");
            } else {
                alert("Por favor, ingrese sus credenciales.");
            }
        },
    },
};
</script>
