import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from app import logger, cf


async def mail_text(target: str, target_name: str, message: str) -> bool:
    try:
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = formataddr((cf.get('mail', 'nickname'), cf.get('mail', 'sender')))
        msg['To'] = formataddr((target_name, target))
        msg['Subject'] = cf.get('mail', 'subject')
        server = smtplib.SMTP(cf.get('mail', 'smtp'), 25)
        server.login(cf.get('mail', 'sender'), cf.get('mail', 'pwd'))
        server.sendmail(cf.get('mail', 'sender'), [target], msg.as_string())
        server.quit()
    except Exception as e:
        logger.error(e)
        return False
    return True
