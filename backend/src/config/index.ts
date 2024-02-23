import { IconCompass, IconDashboard, IconDeviceAnalytics, IconGauge, IconPokeball, InfoCircle } from '@tabler/icons-react';
import { NavItem } from '@/types/nav-item';

export const navLinks: NavItem[] = [
	{ label: 'Getting Started', icon: IconCompass, link: '/dashboard/getting-started' },
	{ label: 'About Page', icon: InfoCircle, link: '/dashboard/about-page'}
	{ label: 'Dashboard', icon: IconDashboard, link: '/dashboard' },

	{
		label: 'Team Builder',
		icon: IconPokeball,
		initiallyOpened: true,
		links: [
			{
				label: 'Overview',
				link: '/dashboard/teambuilder',
			},
			{
				label: 'Archetype',
				link: '/dashboard/teambuilder/archetype',
			},
			{
				label: 'API',
				link: '/dashboard/teambuilder/api',
			}
		],
	},
	{
		label: 'Usage Rate',
		icon: IconGauge,
		initiallyOpened: true,
		links: [
			{
				label: 'Overview',
				link: '/dashboard/usage-rate',
			},
			{
				label: 'API',
				link: '/dashboard/usage-rate/api',
			}
		],
	},
	{
		label: 'Common Movesets',
		icon: IconDeviceAnalytics,
		initiallyOpened: true,
		links: [
			{
				label: 'Overview',
				link: '/dashboard/common-movesets',
			},
			{
				label: 'API',
				link: '/dashboard/common-movesets/api',
			}
		],
	},
];