from TempmailPlus import EmailSendHelper


class TestSendEmailTest:

    def test_sendmail(self, browser):
        self.tempmail_site = EmailSendHelper(browser)
        self.tempmail_site.go_to_site()
        for i in range(15):
            self.tempmail_site.email_address_copy()
            self.tempmail_site.create_and_send_new_test_email()
            i += 1
        self.tempmail_site.create_and_send_summary_test_email()
        for j in range(15):
            self.tempmail_site.delete_test_emails()
            j += 1
