from seleniumbase import SB

with SB(uc=True, incognito=True, test=True) as sb:
    url = "https://pixelscan.net/fingerprint-check"
    sb.activate_cdp_mode(url)
    sb.sleep(3)
    sb.remove_elements(".bg-bannerBg")  # Remove top banner
    sb.remove_elements("pxlscn-ad1")  # Remove an ad banner
    sb.remove_elements("pxlscn-ad2")  # Remove an ad banner
    sb.remove_elements("jdiv")  # Remove chat widgets
    not_masking_text = "You are not masking your fingerprint"
    fp_selector = "pxlscn-fingerprint-masking"
    sb.assert_text(not_masking_text, fp_selector, timeout=15)
    no_automation_detected = "No automation framework detected"
    sb.assert_text(no_automation_detected, "pxlscn-bot-detection")
    consistent_selector = 'div.bg-consistentBg [alt="Good"]'
    sb.highlight(consistent_selector, loops=8)
    sb.sleep(1)
    fingerprint_masking_div = "pxlscn-fingerprint-masking div"
    sb.highlight(fingerprint_masking_div, loops=9)
    sb.sleep(1)
    sb.highlight("pxlscn-bot-detection", loops=10)
    sb.sleep(2)
