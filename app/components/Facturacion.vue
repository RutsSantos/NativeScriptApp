<template>
    <Page>
        <ActionBar title="Facturación" />
        <StackLayout>
            <TextField v-model="invoiceData.client" hint="Cliente" />
            <TextField v-model="invoiceData.amount" hint="Monto" keyboardType="number" />
            <Button :text="isProcessing ? 'Procesando...' : 'Generar Factura'" :isEnabled="!isProcessing" @tap="generateInvoice" />
            <ListView :items="invoices">
                <v-template>
                    <Label :text="'Factura: ' + item.id + ' - ' + item.client + ' $' + item.amount" />
                </v-template>
            </ListView>
        </StackLayout>
    </Page>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
    data() {
        return {
            invoiceData: { client: '', amount: '' }
        };
    },
    computed: {
        ...mapState(['invoices', 'isProcessing'])
    },
    methods: {
        ...mapActions(['processInvoice']),
        generateInvoice() {
            if (this.invoiceData.client && this.invoiceData.amount) {
                this.processInvoice(this.invoiceData);
                this.invoiceData = { client: '', amount: '' };
            }
        }
    }
};
</script>
