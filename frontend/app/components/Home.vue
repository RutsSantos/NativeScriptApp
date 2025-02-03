<!-- <template>
    <Page>
        <ActionBar>
            <Label text="Home"/>
        </ActionBar>

        <GridLayout>
            <Label class="info">
                <FormattedString>
                    <Span class="fas" text.decode="&#xf135; "/>
                    <Span :text="message"/>
                </FormattedString>
            </Label>
        </GridLayout>
    </Page>
</template>

<script>
  export default {
    computed: {
      message() {
        return "Rut's App";
      }
    }
  };
</script>

<style scoped lang="scss">
    @import '@nativescript/theme/scss/variables/blue';

    // Custom styles
    .fas {
        @include colorize($color: accent);
    }

    .info {
        font-size: 20;
        horizontal-align: center;
        vertical-align: center;
    }
</style> -->



<template>
    <Page>
        <ActionBar title="Inicio" />
        <StackLayout>
            <Label text="Bienvenido a la App" />
            <Button text="Ir a Facturación" @tap="goToFacturacion" />
            <Button text="Ver Notificaciones" @tap="goToNotificaciones" />
        </StackLayout>
    </Page>
</template>

<script>
import { navigateTo } from "@/services/navigation";

export default {
    methods: {
        goToFacturacion() {
            navigateTo("Facturacion");
        },
        goToNotificaciones() {
            navigateTo("Notificaciones");
        },
    },
};
</script>
