from mezzanine.conf import register_setting


register_setting(
	name="SOCIAL_LINK_FACEBOOK",
	label="facebook_link_here",
	description="If present a Facebook icon linking here will be in the footer.",
	editable=True,
	default="https://facebook.com",
	)

register_setting(
	name="SOCIAL_LINK_TWITTER",
	label="twitter_link_here",
	description="If present a Twitter icon linking here will be in the footer.",
	editable=True,
	default="https://twitter.com",
	)

register_setting(
	name="SOCIAL_LINK_INSTAGRAM",
	label="instagram_link_here",
	description="If present an Instagram icon linking here will be in the footer.",
	editable=True,
	default="https://instagram.com",
	)

register_setting(
	name="TEMPLATE_ACCESSIBLE_SETTINGS",
	append=True,
	default=("SOCIAL_LINK_FACEBOOK",
				 "SOCIAL_LINK_TWITTER",
				 "SOCIAL_LINK_INSTAGRAM"),
	)
