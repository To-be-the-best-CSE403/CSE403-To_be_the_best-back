import { IconCompass, IconDashboard, IconDeviceAnalytics, IconGauge, IconPokeball } from '@tabler/icons-react';
import { NavItem } from '@/types/nav-item';

export const navLinks: NavItem[] = [
	{ label: 'Getting Started', icon: IconCompass, link: '/dashboard/getting-started' },
	{ label: 'Dashboard', icon: IconDashboard, link: '/dashboard' },

	{
		label: 'Team Builder',
		icon: IconPokeball,
		initiallyOpened: true,
		links: [
			{
				label: 'Best Team',
				link: '/dashboard/best-team',
			},
			{
				label: 'Archetype Team',
				link: '/dashboard/archetype-team',
			},
		],
	},
	{
		label: 'Usage Rate',
		icon: IconGauge,
		initiallyOpened: true,
		links: [
			{
				label: 'API',
				link: '/api/usage-rate',
			},
		],
	},
	{
		label: 'Common Movesets',
		icon: IconDeviceAnalytics,
		initiallyOpened: true,
		links: [
			{
				label: 'API',
				link: '/api/common-movesets',
			},
		],
	},
];