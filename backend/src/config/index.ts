import { IconComponents, IconDashboard, IconLock, IconMoodSmile } from '@tabler/icons-react';
import { NavItem } from '@/types/nav-item';

export const navLinks: NavItem[] = [
	{ label: 'Dashboard', icon: IconDashboard, link: '/dashboard' },

	{
		label: 'Team Builder',
		icon: IconComponents,
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
		icon: IconLock,
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
		icon: IconMoodSmile,
		initiallyOpened: true,
		links: [
			{
				label: 'API',
				link: '/api/common-movesets',
			},
		],
	},
];