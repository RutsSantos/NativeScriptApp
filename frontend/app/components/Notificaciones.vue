<template>
    <Page>
        <ActionBar title="Notificaciones" />
        <StackLayout>
            <Label text="Notificaciones recibidas:" />
            <ListView for="item in notifications">
                <v-template>
                    <Label :text="item.message" />
                </v-template>
            </ListView>
        </StackLayout>
    </Page>
</template>

<script>
export default {
    data() {
        return {
            notifications: [],
        };
    },
    created() {
        this.listenForNotifications();
    },
    methods: {
        listenForNotifications() {
            // Aquí se manejarán las notificaciones push
        },
    },
};
</script>
