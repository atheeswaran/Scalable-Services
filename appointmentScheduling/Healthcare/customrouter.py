class CustomRouter:
    """
    A router to control all database operations on models in the microservices app.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read microservices models go to respective databases.
        """
        if model._meta.app_label == 'RegisterUsers':
            return 'registerusersdb'
        elif model._meta.app_label == 'AppointmentScheduling':
            return 'appointmentdb'
        elif model._meta.app_label == 'Notification':
            return 'notificationdb'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Determine the database alias to use for write operations.
        """
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the same microservice.
        """
        if obj1._meta.app_label in ['RegisterUsers', 'AppointmentScheduling', 'Notification'] and \
           obj2._meta.app_label in ['RegisterUsers', 'AppointmentScheduling', 'Notification']:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that models only appear in the appropriate databases.
        """
        if app_label in ['RegisterUsers', 'AppointmentScheduling', 'Notification']:
            return db in ['registerusersdb', 'appointmentdb', 'notificationdb']
        elif db in ['registerusersdb', 'appointmentdb', 'notificationdb']:
            return False
        return None