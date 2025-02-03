<template>
    <Page>
        <ActionBar title="Facturación" />
        <StackLayout>
            <Label text="Generar Factura" />
            <Button text="Procesar Factura" @tap="procesarFactura" />
            <Label v-if="status" :text="status" />
        </StackLayout>
    </Page>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            status: "",
        };
    },
    methods: {
        async procesarFactura() {
            try {
                let response = await axios.post("http://tu-servidor.com/process-invoice", {
                    user_token: "token_del_usuario",
                });
                this.status = "Factura en proceso: " + response.data.task_id;
            } catch (error) {
                console.error("Error:", error);
                this.status = "Error al procesar factura";
            }
        },
    },
};
</script>
